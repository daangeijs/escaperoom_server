from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from django.db import models
from rooms.wag_views import room_page_view
from django.shortcuts import render

class HomePage(Page):
    body = RichTextField(blank=True)
    template = "rooms/main.html"
    subpage_types = ['RoomPage', 'EmergencyPage']

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]
    
class EmergencyPage(Page):
    body = RichTextField(blank=True)
    template = "rooms/emergency.html"

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]
    
class RoomPage(Page):
    first_stage_body = RichTextField(blank=True)
    second_stage_body = RichTextField(blank=True)
    unlock_key = models.CharField(max_length=255, blank=True, help_text="Key to unlock the room (leave blank if not required)")
    second_stage_unlock_key = models.CharField(max_length=255, blank=True, help_text="Key to unlock the second stage content (leave blank if not required)")

    # Fields for succes and error messages
    first_stage_unlock_success_message = models.TextField(default="First stage successfully unlocked!")
    first_stage_unlock_error_message = models.TextField(default="Incorrect password for the first stage.")
    second_stage_unlock_success_message = models.TextField(default="Second stage successfully unlocked!")
    second_stage_unlock_error_message = models.TextField(default="Incorrect password for the second stage.")

    content_panels = Page.content_panels + [
        FieldPanel('first_stage_body'),
        FieldPanel('unlock_key'),
        FieldPanel('first_stage_unlock_success_message'),
        FieldPanel('first_stage_unlock_error_message'),
        FieldPanel('second_stage_body'),
        FieldPanel('second_stage_unlock_key'),
        FieldPanel('second_stage_unlock_success_message'),
        FieldPanel('second_stage_unlock_error_message'),
    ]
    
    def serve(self, request):
        # Call the view function to get the updated context
        context = room_page_view(request, self)

        # Combine the context from room_page_view with the default context
        full_context = self.get_context(request)
        full_context.update(context)

        # Render the template with the combined context
        return render(request, 'rooms/room.html', full_context)