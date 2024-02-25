def room_page_view(request, page):
    # Initial states from the session or default to True if no key is set
    room_unlocked = not page.unlock_key or request.session.get(f'room_{page.id}_unlocked', False)
    stage_two_unlocked = not page.second_stage_unlock_key or request.session.get(f'stage_two_{page.id}_unlocked', False)
    
    context = {
        'room_unlocked': room_unlocked,
        'stage_two_unlocked': stage_two_unlocked,
        'room_unlock_error': False,  # No error initially
        'stage_two_unlock_error': False,  # No error initially
    }

    if request.method == 'POST':
        if 'action' in request.POST:
            if request.POST['action'] == 'unlock_room':
                if page.unlock_key and request.POST.get('unlock_code') == page.unlock_key:
                    context['room_unlocked'] = True
                    request.session[f'room_{page.id}_unlocked'] = True
                elif page.unlock_key:
                    # Wrong unlock code for first stage
                    context['room_unlock_error'] = True
            elif request.POST['action'] == 'unlock_stage_two':
                if page.second_stage_unlock_key and request.POST.get('stage_two_code') == page.second_stage_unlock_key:
                    context['stage_two_unlocked'] = True
                    request.session[f'stage_two_{page.id}_unlocked'] = True
                elif page.second_stage_unlock_key:
                    # Wrong unlock code for second stage
                    context['stage_two_unlock_error'] = True

    return context
