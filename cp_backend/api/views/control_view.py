import traceback

from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from api.utils.cabinet_modbus_manager import ModbusManager
# Create your views here.


class ControlView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        outdict = {}
        manager = ModbusManager()
        control_point = None
        try:
            control_point = self.request.query_params.get('control')
        except:
            print("no control name found")

        try:
            if control_point:
                outdict.update(manager.read_single_control_point(control_point))
            else:
                outdict.update(manager.get_system_control_points_values())
            # outdict.update(manager.read_single_control_point("active_power"))
        except:
            traceback.print_exc()

        #outdict.update(manager.get_sub_system_control_point_values())
        return Response(data=outdict, status=200)

    def post(self, request):
        try:
            print(request.data)
            sub_system_id = request.data.get("sub_system_id", None)
            control_point = request.data.get("control_point")
            value = request.data.get("value", None)
            value = float(value) if value else None
            print("data: ", request.data)
            manager = ModbusManager()
            if manager.write_or_toggle_control_point(control_point, value, sub_system_id=sub_system_id):
                return Response(data={"message": "control point written successfully.",
                                      control_point: manager.read_single_control_point(control_point).get(control_point)}, status=200)
            else:
                return Response(data={"message": "control point write failed"}, status=500)
        except Exception as e:
            traceback.print_exc()
            return Response(data={"message": str(e)}, status=400)


