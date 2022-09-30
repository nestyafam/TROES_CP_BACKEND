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

        outdict.update(manager.get_system_control_points_values())
        outdict.update(manager.get_sub_system_control_point_values())
        return Response(data=outdict, status=200)

    def post(self, request):
        try:
            print(request.data)
            sub_system_id = request.data.get("sub_system_id", None)
            control_point = request.data.get("control_point")
            value = request.data.get("value")
            manager = ModbusManager()
            if manager.write_or_toggle_control_point(control_point, value, sub_system_id=sub_system_id):
                return Response(data={"message": "control point written successfully."}, status=200)
            else:
                return Response(data={"message": "control point write failed"}, status=500)
        except Exception as e:
            return Response(data={"message": str(e)}, status=400)

