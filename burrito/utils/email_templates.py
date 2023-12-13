
TEMPLATE__ASSIGNED_TO_TICKET = {
    "subject": "Призначення відповідального за тікет #{ticket_id}",
    "content": """
Шановна адміністраціє,

Хочемо повідомити, що Ви були призначені відповідальним на платформі TreS.

Інформація про тікет:
Номер тікета: #{ticket_id}
Тема: {ticket_subject}

З найкращими побажаннями,
Команда TreS
"""
}

TEMPLATE__UNASSIGNED_TO_TICKET = {
    "subject": "Зняття з відповідальності за тікет #{ticket_id}",
    "content": """
Шановна адміністраціє,

Бажаємо повідомити, що з моменту цього листа відповідальність за тікет із номером #{ticket_id} на платформі TreS тепер покладена на іншого представника команди.

Інформація про тікет:
Номер тікета: #{ticket_id}
Тема: {ticket_subject}

З найкращими побажаннями,
Команда TreS
"""
}
