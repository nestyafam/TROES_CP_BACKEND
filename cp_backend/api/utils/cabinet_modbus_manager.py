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
SIMULATION = True
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
                 modbus_ip=system_details["ip"],
                 pcs_ip=system_details["pcs_config"].get("ip"),
                 bms_ip=system_details["bms_config"].get("ip"),
                 arm_ip=system_details["arm_config"].get("ip"),
                 slave_idx=1,
                 modbus_timeout=10.0,
                 bc_count=system_details["bc_count"],
                 bsu_count=system_details["bsu_count"],
                 cell_count=system_details["cell_count"],
                 source_id=None,
                 **kwargs):

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
        self.pcs_ip = pcs_ip
        self.bms_ip = bms_ip
        self.arm_ip = arm_ip
        self.pcs_master = mt.TcpMaster(self.pcs_ip)
        self.bms_master = mt.TcpMaster(self.bms_ip)
        self.arm_master = mt.TcpMaster(self.arm_ip)

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
                        val = round(RTUMultiplier.get_cabinet_multiplier(field) * hold_value[idx], 4)
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
                    val = round(RTUMultiplier.get_cabinet_multiplier(field) * hold_value[idx], 4)
                    return_dict.update({field: val})

            print("dict: ", return_dict)
            # print("len of hvac_dict: ", len(hvac_dict))
        except Exception as e:
            print("modbus fetch error: ", str(e))
            traceback.print_exc()
        return return_dict

    def read_single_control_point(self, control_point, **kwargs):
        master = mt.TcpMaster(self.modbus_ip)
        if control_point in system_fields.keys():
            address = system_fields[control_point].get("address")
            data = self.get_modbus_data(master, fields=[control_point], starting_address=address)
        elif control_point in sub_system_fields.keys():

            sub_system_id = kwargs.get("sub_system_id", None)
            if not sub_system_id:
                print("here2")
                raise Exception("Enter sub system id")
            else:
                address = sub_system_fields[control_point].get("address") + \
                          (sub_system_id * sub_system_fields[control_point].get("multiplier"))
                data = self.get_modbus_data(master, fields=[control_point], starting_address=address)
        print("data: ", data)
        return data[control_point]

    def get_system_control_points_values(self):
        master = mt.TcpMaster(self.modbus_ip)
        outdict = {}
        for control_point, address_details in system_fields.items():
            fields = []
            if address_details["length"] == 2:
                fields = [control_point, control_point + "_first"]
            else:
                fields = [control_point]
            data = self.get_modbus_data(master, fields=fields, starting_address=address_details["address"])
            outdict.update(data)
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

    def write_single_register(self, address, value, simulation=SIMULATION):
        """Write the values of a single register and check that it is correctly written"""
        if simulation:
            return True
        result = self.master.execute(self.slave_idx, md.WRITE_SINGLE_REGISTER, address, output_value=value)
        read_result = self.master.execute(self.slave_idx, md.READ_HOLDING_REGISTERS, address, 1)
        self.assertEqual(result, read_result)

        return result == read_result

    def write_multiple_registers(self, address, values, simulation=SIMULATION):
        if simulation:
            return True
        result = self.master.execute(self.slave_idx, md.WRITE_MULTIPLE_REGISTERS, address, output_value=values)
        read_result = self.master.execute(self.slave_idx, md.READ_HOLDING_REGISTERS, address, len(values))
        self.assertEqual(result, read_result)

        return result == read_result

    def write_or_toggle_control_point(self, control_point, value, **kwargs):

        if control_point in system_fields.keys():
            current_value = self.read_single_control_point(control_point)
            if "toggle_values" in system_fields[control_point].keys():
                toggle_values = system_fields[control_point].get("toggle_values")
                value = toggle_values[1 - toggle_values.index(current_value)]
            address = system_fields[control_point].get("address")
            return self.write_single_register(address, value)

        elif control_point in sub_system_fields.keys():

            sub_system_id = kwargs.get("sub_system_id", None)

            if sub_system_id is not None:
                current_value = self.read_single_control_point(control_point, sub_system_id=sub_system_id)
                if "toggle_values" in sub_system_fields[control_point].keys():
                    toggle_values = sub_system_fields[control_point].get("toggle_values")
                    value = toggle_values[1 - toggle_values.index(current_value)]
                address = sub_system_fields[control_point].get("address") + \
                          sub_system_fields[control_point].get("multiplier") * sub_system_id
                return self.write_single_register(address, value)
            else:
                raise Exception("enter sub_system_id")


if __name__ == "__main__":
    manager = ModbusManager()
    print(manager.get_system_control_points_values())
    print(manager.get_sub_system_control_point_values())
    print(manager.write_control_point("km1", 1, 1))
