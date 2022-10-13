import logging
from builtins import complex

import modbus_tk.modbus_tcp as mt
import modbus_tk.defines as md
import os
from django.conf import settings
import django
import traceback
from cabinet_multipliers import RTUMultiplier

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cp_backend.cp_backend.settings")
django.setup()
SIMULATION = False
sub_system_fields = settings.SUB_SYSTEM_FIELDS
system_fields = settings.SYSTEM_FIELDS
system_details = settings.SYSTEM_DETAILS


def getSignedNumber(number, bitLength):
    mask = (2 ** bitLength) - 1
    if number & (1 << (bitLength - 1)):
        return number | ~mask
    else:
        return number & mask


def get_unsigned_number(value, bit_length):
    return (2 ** bit_length) - value


def parse_signed_16bits_dec_value(val):
    print("unsigned int: ", val)
    sign = '{0:016b}'.format(val)[0]
    if sign == '1':
        val = -((val ^ 0xFFFF) + 1)
    return val


class ModbusManager:
    """
    class for new systems 8 and 9
    """
    logger = logging.getLogger('django')
    max_regs_per_request = 100

    def __init__(self,
                 modbus_ip=None,
                 pcs_details=None,
                 bms_details=None,
                 arm_details=None,
                 slave_idx=1,
                 modbus_timeout=10.0,
                 bc_count=system_details["bc_count"],
                 bsu_count=system_details["bsu_count"],
                 cell_count=system_details["cell_count"],
                 source_id=None,
                 **kwargs):
        if modbus_ip is None:
            self.modbus_ip = system_details["ip"]
        if bms_details is None:
            self.bms_details = {
                "ip": system_details["bms"].get("ip"),
                "port": system_details["bms"].get("ip")
            }
        if arm_details is None:
            self.arm_details = {
                "ip": system_details["arm"].get("ip"),
                "port": system_details["arm"].get("ip")
            }
        if pcs_details is None:
            self.pcs_details = {
                "ip": system_details["pcs"].get("ip"),
                "port": system_details["pcs"].get("ip")
            }
        self.modbus_ip = modbus_ip
        self.slave_idx = slave_idx
        self.modbus_timeout = modbus_timeout
        # battery cluster count
        self.bc_count = bc_count
        # battery pack count per cluster
        self.bsu_count = bsu_count
        # battery cell count per pack
        self.cell_count = cell_count
        self.source_id = source_id

    def get_modbus_data(self, master, fields, starting_address, simulation=SIMULATION):
        hold_value = None
        return_dict = {}
        if simulation:
            for x in fields:
                if x not in ["spare", "reserved", "reserve"]:
                    return_dict.update({x: 0})
            return return_dict
        try:
            no_holding_addr = len(fields)
            # print("no of reg to read: ", no_holding_addr)
            reps = int(no_holding_addr / self.max_regs_per_request)
            remainder = no_holding_addr - (reps * self.max_regs_per_request)
            temp_starting_address = starting_address
            temp_fields_start_index = 0
            for i in range(0, reps):
                temp_starting_address = starting_address + (i * self.max_regs_per_request)
                print("starting address: ", temp_starting_address)
                hold_value = master.execute(slave=self.slave_idx, function_code=md.READ_HOLDING_REGISTERS,
                                            starting_address=temp_starting_address,
                                            quantity_of_x=self.max_regs_per_request, output_value=no_holding_addr)
                # print("len of hold_val: ", len(hold_value))
                temp_fields_start_index = i * self.max_regs_per_request
                temp_fields = fields[
                              temp_fields_start_index:temp_fields_start_index + self.max_regs_per_request]
                print("len of temp fields: ", len(fields))
                for idx, field in enumerate(temp_fields):

                    if field.lower() not in ["spare", "reserved", "reserve"]:
                        print("field: ", field)
                        val = round(RTUMultiplier.get_cabinet_multiplier(field) * getSignedNumber(hold_value[idx], 16),
                                    4)
                        return_dict.update({field: val})
            hold_value = master.execute(slave=self.slave_idx, function_code=md.READ_HOLDING_REGISTERS,
                                        starting_address=temp_starting_address,
                                        quantity_of_x=remainder, output_value=no_holding_addr)
            # print("len of hold_val: ", hold_value)
            # if there are less than max regs count
            if temp_fields_start_index != 0:
                temp_fields_start_index += self.max_regs_per_request
            temp_fields = fields[
                          temp_fields_start_index:(temp_fields_start_index + remainder)]
            # print("len of temp fields: ", len(temp_hvac_fields))
            for idx, field in enumerate(temp_fields):
                if field.lower() not in ["spare", "reserved", "reserve"]:
                    print("field: ", field)
                    val = round(RTUMultiplier.get_cabinet_multiplier(field) * getSignedNumber(hold_value[idx], 16), 4)
                    return_dict.update({field: val})

            print("dict: ", return_dict)
            # print("len of hvac_dict: ", len(hvac_dict))
        except Exception as e:
            print("modbus fetch error: ", str(e))
            traceback.print_exc()
        return return_dict

    def read_single_control_point(self, control_point, **kwargs):
        field_types = ["pcs", "bms", "arm"]
        for field_type in field_types:
            master = mt.TcpMaster(host=system_details[field_type].get("ip"),
                                  port=system_details[field_type].get("port"))
            system_field_details = system_fields[field_type]
            sub_system_field_details = sub_system_fields[field_type]
            print(system_field_details.keys())
            if control_point in system_field_details.keys():
                print("system field")
                control_point_details = system_field_details[control_point]
                print("control point details: ", control_point_details)
                address = system_field_details[control_point].get("address")
                print("address: ", address)
                data = self.get_modbus_data(master, fields=[control_point], starting_address=address)
            elif control_point in sub_system_field_details.keys():
                print("sub system field")
                if kwargs.get("bmu_no", None) is not None:
                    control_point_details = sub_system_field_details[control_point]
                    address = control_point_details["address"] + (control_point_details["multiplier"] *
                                                                  kwargs.get("bmu_no"))
                    try:
                        data = self.get_modbus_data(master, fields=[control_point],
                                                    starting_address=address, simulation=False)
                    except Exception as e:
                        print("Exception :", str(e))
                        data = None
                    print("data: ", data)
                else:
                    return None
        # if control_point in system_fields.keys():
        #     address = system_fields[control_point].get("address")
        #     data = self.get_modbus_data(master, fields=[control_point], starting_address=address)
        # elif control_point in sub_system_fields.keys():
        #
        #     sub_system_id = kwargs.get("sub_system_id", None)
        #     if not sub_system_id:
        #         print("here2")
        #         raise Exception("Enter sub system id")
        #     else:
        #         address = sub_system_fields[control_point].get("address") + \
        #                   (sub_system_id * sub_system_fields[control_point].get("multiplier"))
        #         data = self.get_modbus_data(master, fields=[control_point], starting_address=address)
        print("data: ", data)
        return data if data else {control_point: None}

    def get_system_control_points_values(self):

        outdict = {}
        field_types = ["pcs", "bms", "arm"]
        for field_type in field_types:
            field_details = system_fields[field_type]
            master = mt.TcpMaster(host=system_details[field_type].get("ip"),
                                  port=system_details[field_type].get("port"))
            outdict[field_type] = {}
            for control_point, point_details in field_details.items():
                fields = [control_point]
                data = self.get_modbus_data(master, fields=fields, starting_address=point_details["address"],
                                            simulation=False)
                outdict[field_type].update(data)
        return outdict

    def get_sub_system_control_point_values(self, sub_system_id=-1):
        master = mt.TcpMaster(self.modbus_ip)
        outdict = {}
        if sub_system_id != -1:
            for control_point, address_details in sub_system_fields.items():
                data = self.get_modbus_data(master, fields=[control_point],
                                            starting_address=(address_details["address"]) +
                                                             (int(sub_system_id) * address_details["multiplier"]))
                outdict.update(data)
        else:

            for sub_system_id in range(1, self.bc_count + 1):
                sub_system_data = {}
                print("getting subsystem values for ", sub_system_id)
                for control_point, address_details in sub_system_fields.items():
                    sub_system_data.update(self.get_modbus_data(master, fields=[control_point],
                                                                starting_address=(address_details["address"]) +
                                                                                 (int(sub_system_id) * address_details[
                                                                                     "multiplier"])))
                outdict.update({sub_system_id: sub_system_data})
        return outdict

    def write_single_register(self, master, address, value, simulation=SIMULATION):
        """Write the values of a single register and check that it is correctly written"""
        if simulation:
            return True
        result = master.execute(self.slave_idx, md.WRITE_SINGLE_REGISTER, address, output_value=value)
        print("result: ", result)
        read_result = master.execute(self.slave_idx, md.READ_HOLDING_REGISTERS, address, 1)[0]
        print("read result: ", read_result)
        return read_result == value

    def write_multiple_registers(self, address, values, simulation=SIMULATION):
        if simulation:
            return True
        result = self.master.execute(self.slave_idx, md.WRITE_MULTIPLE_REGISTERS, address, output_value=values)
        read_result = self.master.execute(self.slave_idx, md.READ_HOLDING_REGISTERS, address, len(values))
        return result == read_result

    def get_pcs_status(self, master, control_point_details):
        read_result = master.execute(self.slave_idx, md.READ_HOLDING_REGISTERS, control_point_details["address"], 1)
        return read_result[0]

    def write_or_toggle_control_point(self, control_point, value, **kwargs):
        for field_type in ["pcs", "arm", "bms"]:
            master = mt.TcpMaster(host=system_details[field_type].get("ip"),
                                  port=system_details[field_type].get("port"))
            if control_point in system_fields[field_type].keys():
                if control_point == "pcs_toggle":
                    current_value = self.get
                current_value = self.read_single_control_point(control_point).get(control_point, None)
                print("current val: ", current_value)
                control_point_details = system_fields[field_type].get(control_point, None)
                if control_point_details:
                    print("control point details: ", control_point_details)
                    if "toggle_values" in control_point_details.keys():
                        toggle_values = control_point_details.get("toggle_values")
                        value = toggle_values[1 - toggle_values.index(current_value)]
                        print("toggle value: ", value)
                    address = control_point_details.get("address")
                    print("address to write: ", address)
                    return self.write_single_register(master, address, value)

            elif control_point in sub_system_fields[field_type].keys():

                sub_system_id = kwargs.get("sub_system_id", None)

                if sub_system_id is not None:
                    current_value = self.read_single_control_point(control_point, sub_system_id=sub_system_id)
                    if "toggle_values" in sub_system_fields[control_point].keys():
                        toggle_values = sub_system_fields[control_point].get("toggle_values")
                        value = toggle_values[1 - toggle_values.index(current_value)]
                    address = sub_system_fields[control_point].get("address") + \
                              sub_system_fields[control_point].get("multiplier") * sub_system_id
                    return self.write_single_register(master, address, value)
                else:
                    raise Exception("enter sub_system_id")


if __name__ == "__main__":
    manager = ModbusManager()
    print(manager.get_system_control_points_values())
    # print(manager.get_sub_system_control_point_values())
    # print(manager.write_control_point("km1", 1, 1))
