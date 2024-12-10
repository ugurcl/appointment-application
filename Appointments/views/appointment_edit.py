from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import AppointmentCreation, AppointmentDetails
from User.send_mail import send_email_with_template

class EditAppointmentVerifiedUser(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        appointment_id = kwargs.get('id')
        try:
            appointment = AppointmentDetails.objects.get(id=appointment_id)
            user = appointment.customer.user
            status = request.POST.get('status')

            if status == 'Onaylandı':
                send_email_with_template(
                    user=user,
                    subject=f'Randevunuz {status}',
                    message=f'{appointment.appointment.staff_member.user.get_full_name()} Adlı öğretim görevlisinden aldığınız randevu onaylanmıştır. ',
                    from_mail=user.email,
                    link=None
                )
            elif status == 'İptal Edildi':
                appointment_creation = appointment.appointment
        
                appointment_creation.appointment_is_active = True
                appointment_creation.save()
                send_email_with_template(
                    user=user,
                    subject=f'Randevunuz {status}',
                    message=f'{appointment.appointment.staff_member.user.get_full_name()} Adlı öğretim görevlisinden aldığınız randevu iptal edilmiştir. ',
                    from_mail=user.email,
                    link=None
                )
            appointment.status = status
            appointment.save()

        except AppointmentDetails.DoesNotExist:
            
            return redirect('user_appointment_list')  

        return redirect('user_appointment_list')