import traceback

from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from api.utils.cabinet_modbus_manager import ModbusManager


# Create your views here.


class MonitorView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            data = request.data
            request_type = data.get("request_type", None)
            response_data = {}
            if request_type == "cluster":

                response_data["clusters_data"] = [
                    {
                        "image":
                            "./assets/img/psotwkbdo0qm9x3aamhgnzemakz7arke6tga20679f1-c016-4b20-b8cc-df5a9668237e.png",
                        "state": "Normal",
                        "clusters_soc": "70%",
                        "total_pressure": "768V",
                        "soh_cluster": "99%",
                    },
                    {
                        "image":
                            "./assets/img/psotwkbdo0qm9x3aamhgnzemakz7arke6tga20679f1-c016-4b20-b8cc-df5a9668237e.png",
                        "state": "Normal",
                        "clusters_soc": "70%",
                        "total_pressure": "768V",
                        "soh_cluster": "99%",
                    },
                    {
                        "image":
                            "./assets/img/psotwkbdo0qm9x3aamhgnzemakz7arke6tga20679f1-c016-4b20-b8cc-df5a9668237e.png",
                        "state": "Normal",
                        "clusters_soc": "70%",
                        "total_pressure": "768V",
                        "soh_cluster": "99%",
                    },
                ]
                response_data["clusters_overview"] = [
                    {"highest_battery_cluster_voltage": "768V"},
                    {"minimum_battery_cluster_voltage": "762V"},
                    {"average_total_battery_cluster_pressure": "764V",
                     },
                    {"differential_pressure": "6V"},
                    {"max_cell_temp": "32"},
                    {"min_cell_temp": "29"},
                    {"avg_cell_temp": "31"},
                    {"cell_temp_diff": "3"},
                ]

            elif request_type == "module":
                cluster_id = data.get("cluster_id")
                response_data["modules_data"] = []
                for i in range(1, 17):
                    response_data["modules_data"].append(
                        {"module_no": i,
                         "module_voltage": 3.2,
                         "operating_status": "normal"})
            elif request_type == "general":
                response_data["system_data"] = {
                    "operating_mode": "grid-connected",
                    "application": "Forward Town",
                    "installed_capacity": "554 KWH",
                    "most_powerful": "250 KWH",
                    "operating_power": "200 KWH",
                    "system_state": "discharging",
                    "cumulative_cycle": "655 times",
                    "soc_percentage": "70%",
                    "soh_percentage": "90%",
                }
                response_data["operating_status_data"] = {
                    "battery_cluster_status": "abnormal",
                    "battery_cluster_1": "normal",
                    "battery_cluster_2": "normal",
                    "battery_cluster_3": "abnormal",
                    "battery_cluster_4": "normal",
                    "pcs_running_status": "normal",
                    "pcs_operating_mode": "grid",
                    "air_conditioner_status": "normal",
                    "fan_status": "normal",
                    "cabinet_environment_status": "normal",
                    "remote_monitoring_status": "normal",
                    "migrid_operator_state": "normal",
                }
                response_data["battery_data"] = {
                    "cumulative_charging_capacity": 35.2,
                    "cumulative_discharge_capacity": 35.12,
                    "max_cell_voltage": 3.7,
                    "minimum_cell_voltage": 2.6
                }
                response_data["environment_data"] = {
                    "highest_cabinet_temp": 34.5,
                    "lowest_cabinet_temp": 31.3,
                    "lowest_cabinet_humidity": 12.3,
                    "highest_cabinet_humidity": 41.7,
                    "noise": 60,
                    "GHG_emission": 500
                }
                response_data["pcs_data"] = {
                    "ac_active_power": 200,
                    "ac_reactive_power": 20,
                    "accumulated_ac_charging_power": 35.43,
                    "accumulated_ac_discharging_power": 34.89
                }
            elif request_type == "historic_cluster":
                cluster_id = data.get("cluster_id")
                response_data = []
                for i in range(1, 17):
                    response_data.append({
                        "module_no": i,
                        "module_voltage": 2.4,
                        "module_temperature": 34.5,
                        "running_state": "normal",
                        "label": ["c", "d", "e", "f", "g", "h", "i"],
                        "y1_data": [1, 2, 3, 4, 5, 6, 7],
                        "y2_data": [7, 8, 2, 10, 7, 12, 11]
                    })



            else:
                return Response(data={"message": "request type found"}, status=400)
            return Response(data=response_data, status=200)
        except Exception as e:
            traceback.print_exc()
            return Response(data={"message": str(e)}, status=400)
