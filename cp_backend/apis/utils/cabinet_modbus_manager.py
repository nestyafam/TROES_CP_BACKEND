import logging
from builtins import complex

import modbus_tk.modbus_tcp as mt
import modbus_tk.defines as md
import os
from django.conf import settings
import django
import traceback
from .cabinet_multipliers import get_cabinet_multiplier
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
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
                 slave_idx=1,
                 modbus_timeout=10.0,
                 bc_count=system_details["bc_count"],
                 bsu_count=system_details["bsu_count"],
                 cell_count=system_details["cell_count"],
                 source_id=None):
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
                        val = round(get_cabinet_multiplier(field) * hold_value[idx], 4)
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
                    val = round(get_cabinet_multiplier(field) * hold_value[idx], 4)
                    return_dict.update({field: val})

            print("dict: ", return_dict)
            # print("len of hvac_dict: ", len(hvac_dict))
        except Exception as e:
            print("modbus fetch error: ", str(e))
            traceback.print_exc()
        return return_dict

    def get_cell_voltage(self, starting_address=100):
        '''
        output: {
            '1': {
                'bsu1_cell1_voltage': 3.2,
                'bsu1_cell2_voltage': 3.2,
                .
                .
                .
                'bsu12_cell16_voltage': 3.2
            },
            .
            .
            .

        }
        '''
        master = mt.TcpMaster(self.modbus_ip)
        master.set_timeout(self.modbus_timeout)
        fields = []
        voltage_dict = {}
        for i in range(1, self.bc_count + 1):
            fields = []

            for j in range(1, self.bsu_count + 1):
                for k in range(1, self.cell_count + 1):
                    fields.append("{bcu_no}bc_{bsu_no}bp_{cell_no}b_voltage".format(bcu_no=i, bsu_no=j, cell_no=k))
            voltage_dict.update({i: self.get_modbus_data(master=master, fields=fields,
                                                         starting_address=starting_address)})
            starting_address += self.bsu_count * self.cell_count
        return voltage_dict

    def get_cell_temperature(self, starting_address=19200):
        master = mt.TcpMaster(self.modbus_ip)
        master.set_timeout(self.modbus_timeout)
        fields = []
        temperature_dict = {}
        for i in range(1, self.bc_count + 1):
            fields = []
            for j in range(1, self.bsu_count + 1):
                for k in range(1, self.cell_count + 1):
                    fields.append("{bcu_no}bc_{bsu_no}bp_{cell_no}b_temperature".format(bcu_no=i, bsu_no=j, cell_no=k))
            temperature_dict.update({i: self.get_modbus_data(master=master, fields=fields,
                                                             starting_address=starting_address)})
            starting_address += self.bsu_count * self.cell_count
        return temperature_dict

    def get_bmu_board_temp(self):
        pass

    def get_bmu_balance_temp(self):
        pass

    def get_bmu_balance_state(self):
        pass

    def get_all_bcu_data(self, fields=[], starting_address=50000):
        master = mt.TcpMaster(self.modbus_ip)
        master.set_timeout(self.modbus_timeout)
        bcu_data_dict = {}
        temp_starting_address = starting_address
        for i in range(0, self.bc_count):
            temp_starting_address = (i * 200) + starting_address
            bcu_data_dict.update({
                (i + 1): self.get_modbus_data(master, fields, temp_starting_address)
            })
        return bcu_data_dict

    def get_bams_data(self, fields=[], starting_address=62000):
        master = mt.TcpMaster(self.modbus_ip)
        master.set_timeout(self.modbus_timeout)
        bams_data_dict = {}
        bams_data_dict.update(self.get_modbus_data(master, fields, starting_address))
        bams_data_dict["BamsMinCellVBcuNo"] = 0
        bams_data_dict["BamsMaxCellVBcuNo"] = 0
        bams_data_dict["BamsMinCellVBmuNo"] = 0
        bams_data_dict["BamsMaxCellVBmuNo"] = 0
        bams_data_dict["BamsMaxCellTBcuNo"] = 0
        bams_data_dict["BamsMinCellTBcuNo"] = 0
        bams_data_dict["BamsMaxCellTBmuNo"] = 0
        bams_data_dict["BamsMinCellTBmuNo"] = 0
        return bams_data_dict

    def get_bams_esu_data(self, fields=[], starting_address=62500):
        master = mt.TcpMaster(self.modbus_ip)
        master.set_timeout(self.modbus_timeout)
        bams_ems_data_dict = {}
        bams_ems_data_dict.update(self.get_modbus_data(master, fields, starting_address))
        return bams_ems_data_dict

    def fetch_bcu_data(self,
                       bcu_no,
                       bcu_data_starting_address,
                       voltage_starting_address,
                       temperature_starting_address):
        bcu_data_config = fields_data["bcu_data"]
        output_dict = {}
        all_bcu_data = self.get_all_bcu_data(fields=bcu_data_config['fields'],
                                             starting_address=bcu_data_starting_address)
        output_dict.update({"bcu_data": all_bcu_data[bcu_no]})
        voltage_data = self.get_cell_voltage(starting_address=voltage_starting_address)
        output_dict.update({"voltage_data": voltage_data[bcu_no] if voltage_data[bcu_no] is not None else {}})
        temperature_data = self.get_cell_temperature(starting_address=temperature_starting_address)
        output_dict.update(
            {"temperature_data": temperature_data[bcu_no] if temperature_data[bcu_no] is not None else {}})
        all_hvac_data = self.fetch_hvac_data()
        output_dict.update({"hvac_data": all_hvac_data[bcu_no]})
        return output_dict

    def fetch_hvac_data(self):
        master = mt.TcpMaster(self.modbus_ip)
        master.set_timeout(self.modbus_timeout)
        output_dict = {}

        for i in range(1, self.bc_count):
            hvac_bcu_data = {}
            for hvac_field_details in fields_data["hvac_data"]:
                starting_address = hvac_field_details["starting_address"]
                temp_data = self.get_modbus_data(master, fields=hvac_field_details["fields"],
                                                 starting_address=starting_address)
                hvac_bcu_data.update(temp_data)
                starting_address += (i * hvac_field_details["multiplier"])
            output_dict.update({
                i: hvac_bcu_data
            })
        return output_dict

    def fetch_system_data(self, starting_address=62000):
        print("fetching system data for cabinet systems")
        master = mt.TcpMaster(self.modbus_ip)
        master.set_timeout(self.modbus_timeout)
        output_dict = {}
        bams_field_details = fields_data["bams_data"]
        fields = bams_field_details["fields"]
        temp_fields = fields
        for index in range(len(fields)):
            if fields.count(fields[index]) > 1:
                fields[index] = fields[index] + "_first"

        output_dict = self.get_bams_data(fields=fields, starting_address=starting_address)
        output_dict["system_current_A_signed"] = output_dict["BamsCurrent"]
        output_dict["sys_highest_cell_temperature_oC_signed"] = output_dict["BamsMaxCellT"]
        output_dict["sys_lowest_cell_temperature_oC_signed"] = output_dict["BamsMinCellT"]
        output_dict["system_voltage_V"] = output_dict["BamsVoltage"]
        print("output dict in fetch_system_data for cabinet systems")
        return output_dict

    def get_pcs_system_status(self):
        fields = ["sys_status", "ac_status", "reserve", "charging_status"]
        master = mt.TcpMaster(self.modbus_ip)
        master.set_timeout(self.modbus_timeout)
        data = self.get_modbus_data(master, fields, 53010)
        for key, dec_data in data.items():
            print(dec_data)
            bin_data = format(dec_data,'016b')
            data[key] = bin_data
        outdict = {}
        outdict["system_on_off_status"] = int(data["sys_status"][0])
        outdict["system_grid_tied"] = int(data["sys_status"][2])
        outdict["system_off_grid"] = int(data["sys_status"][3])
        outdict["system_ac_switch_status"] = int(data["ac_status"][8])
        outdict["system_warning_status"] = int(data["ac_status"][9])
        outdict["system_fault_status"] = int(data["ac_status"][10])
        outdict["dc_string_1_charging"] = int(data["charging_status"][2])
        outdict["dc_string_1_discharging"] = int(data["charging_status"][3])
        return outdict

    def get_pcs_alarms(self):
        fields = ["pcs_faults"]
        master = mt.TcpMaster(self.modbus_ip)
        master.set_timeout(self.modbus_timeout)
        data = self.get_modbus_data(master, fields, 53000)
        pcs_faults = format(data["pcs_faults"],'016b')

        # eg: pcs_faults = 0000000011111111
        # dc_ac_subsystem_ac_over_voltage_abnormal = pcs_faults[0]
        fault_register_value_index_map = {
            0: "dc_ac_subsystem_ac_over_voltage_abnormal",
            1: "dc_ac_subsystem_ac_over_frequency_abnormal",
            2: "dc_ac_subsystem_ac_under_voltage_abnormal",
            3: "dc_ac_subsystem_islanding_abnormal",
            4: "dc_ac_subsystem_dc_input_over_voltage_abnormal",
            5: "dc_ac_subsystem_grid_tied_off_grid_switching_failed_abnormal",
            6: "dc_ac_subsystem_ac_phase_reversed_abnormal",
            7: "dc_ac_subsystem_dc_input_under_voltage_abnormal",
            8: "dc_ac_subsystem_over_load_alarm",
            9: "dc_ac_subsystem_ac_output_voltage_fault",
            10: "dc_ac_subsystem_ac_phase_lost_fault",
            11: "dc_ac_subsystem_grid_voltage_unbalanced_abnormal",
            12: "dc_ac_subsystem_ac_under_frequency_abnormal",
            13: "dc_ac_subsystem_micro_grid_battery_low_soc_abnormal",
            15: "dc_ac_subsystem_off_grid_ac_voltage_phase_reversed_abnormal"
        }
        outdict = {}
        for index, value in fault_register_value_index_map.items():
            outdict.update({
                value: int(pcs_faults[index])
            })
        return outdict




