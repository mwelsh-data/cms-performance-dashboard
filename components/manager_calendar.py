from datetime import date, datetime, time, timedelta

import streamlit as st
from streamlit_calendar import calendar


OUTLOOK_CALENDAR_URL = "https://outlook.office.com/calendar/view/month"


def initialize_calendar_state():
    if "manager_calendar_events" not in st.session_state:
        st.session_state.manager_calendar_events = []

    if "show_calendar_event_form" not in st.session_state:
        st.session_state.show_calendar_event_form = False


def add_event_form():
    st.subheader("Add Calendar Event")

    default_start = datetime.now().replace(
        minute=0,
        second=0,
        microsecond=0,
    ) + timedelta(hours=1)

    with st.form("manager_calendar_event_form", clear_on_submit=True):
        title = st.text_input(
            "Event title",
            placeholder="Example: Smith family move",
        )

        description = st.text_area(
            "Description",
            placeholder="Crew, truck, addresses, customer notes, or other details",
        )

        location = st.text_input(
            "Location",
            placeholder="Example: 123 Main Street",
        )

        all_day = st.checkbox("All-day event")

        col1, col2 = st.columns(2)

        with col1:
            start_date = st.date_input(
                "Start date",
                value=default_start.date(),
            )

            start_time = st.time_input(
                "Start time",
                value=default_start.time(),
                disabled=all_day,
            )

        with col2:
            end_date = st.date_input(
                "End date",
                value=default_start.date(),
            )

            end_time = st.time_input(
                "End time",
                value=(default_start + timedelta(hours=2)).time(),
                disabled=all_day,
            )

        submit_col, cancel_col = st.columns(2)

        with submit_col:
            submitted = st.form_submit_button(
                "Save Event",
                type="primary",
                use_container_width=True,
            )

        with cancel_col:
            cancelled = st.form_submit_button(
                "Cancel",
                use_container_width=True,
            )

    if cancelled:
        st.session_state.show_calendar_event_form = False
        st.rerun()

    if not submitted:
        return

    if not title.strip():
        st.error("Please enter an event title.")
        return

    if all_day:
        if end_date < start_date:
            st.error("The end date cannot be before the start date.")
            return

        event_start = start_date.isoformat()

        # FullCalendar treats an all-day end date as exclusive.
        event_end = (end_date + timedelta(days=1)).isoformat()
    else:
        event_start_datetime = datetime.combine(start_date, start_time)
        event_end_datetime = datetime.combine(end_date, end_time)

        if event_end_datetime <= event_start_datetime:
            st.error("The event must end after it starts.")
            return

        event_start = event_start_datetime.isoformat()
        event_end = event_end_datetime.isoformat()

    event = {
        "id": f"event-{datetime.now().timestamp()}",
        "title": title.strip(),
        "start": event_start,
        "end": event_end,
        "allDay": all_day,
        "extendedProps": {
            "description": description.strip(),
            "location": location.strip(),
        },
    }

    st.session_state.manager_calendar_events.append(event)
    st.session_state.show_calendar_event_form = False

    st.success("Event added successfully.")
    st.rerun()


def render_manager_calendar(portal_name="Manager"):
    initialize_calendar_state()

    st.markdown(
        f'<a class="back-link" href="?view=menu">'
        f"← Back to {portal_name} Portal"
        "</a>",
        unsafe_allow_html=True,
    )

    st.title(f"{portal_name} Calendar")
    st.caption("View company jobs and events by month, week, or day.")

    outlook_col, add_col = st.columns([1, 1])

    with outlook_col:
        st.link_button(
            "Open Outlook Calendar",
            OUTLOOK_CALENDAR_URL,
            use_container_width=True,
        )

    with add_col:
        if st.button(
            "＋ Add Event",
            type="primary",
            use_container_width=True,
        ):
            st.session_state.show_calendar_event_form = True

    if st.session_state.show_calendar_event_form:
        add_event_form()

    calendar_options = {
        # Monthly is the default view.
        "initialView": "dayGridMonth",
        "height": 720,
        "firstDay": 0,
        "nowIndicator": True,
        "navLinks": True,
        "editable": False,
        "selectable": True,
        "dayMaxEvents": True,

        # FullCalendar provides previous, next, and today controls here.
        "headerToolbar": {
            "left": "prev,next today",
            "center": "title",
            "right": "dayGridMonth,timeGridWeek,timeGridDay",
        },

        # Friendly labels for the view buttons.
        "buttonText": {
            "today": "Today",
            "month": "Month",
            "week": "Week",
            "day": "Day",
        },
    }

    custom_css = """
    .fc {
        background: white;
        color: #1f2937;
        border-radius: 18px;
        padding: 18px;
    }

    .fc .fc-toolbar-title {
        color: #000080;
        font-size: 1.6rem;
        font-weight: 700;
    }

    .fc .fc-button-primary {
        background-color: #000080;
        border-color: #000080;
    }

    .fc .fc-button-primary:hover {
        background-color: #1111a8;
        border-color: #1111a8;
    }

    .fc .fc-button-primary:not(:disabled).fc-button-active {
        background-color: #1111a8;
        border-color: #1111a8;
    }

    .fc .fc-event {
        background-color: #000080;
        border-color: #000080;
        cursor: pointer;
    }

    .fc .fc-daygrid-day-number,
    .fc .fc-col-header-cell-cushion {
        color: #1f2937;
        text-decoration: none;
    }
    """

    calendar_result = calendar(
        events=st.session_state.manager_calendar_events,
        options=calendar_options,
        custom_css=custom_css,
        key="manager_calendar",
    )

    selected_event = calendar_result.get("eventClick")

    if selected_event:
        event_data = selected_event.get("event", {})
        extended = event_data.get("extendedProps", {})

        with st.expander(
            f"Selected event: {event_data.get('title', 'Event')}",
            expanded=True,
        ):
            st.write(f"**Starts:** {event_data.get('start', 'Not provided')}")
            st.write(f"**Ends:** {event_data.get('end', 'Not provided')}")

            if extended.get("location"):
                st.write(f"**Location:** {extended['location']}")

            if extended.get("description"):
                st.write(f"**Description:** {extended['description']}")

    if not st.session_state.manager_calendar_events:
        st.info(
            "No events have been added yet. Select “Add Event” to create one."
        )