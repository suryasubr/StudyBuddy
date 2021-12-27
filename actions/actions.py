# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher


class action_service(Action):

    def name(self) -> Text:
        return "action_service"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons=[
            {"payload":'/lecture{"content_type":"lecture"}', "title": "Lectures"},
            {"payload":'/deliverable{"content_type":"deliverable"}', "title": "Deliverables"}
        ]
        dispatcher.utter_message(text="Choose a topic for which you need my assistance", buttons=buttons)

        return []


class action_lectures(Action):

    def name(self) -> Text:
        return "action_lectures"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons=[
            {"payload":'/lecture1{"lecture_type":"lecture1"}', "title": "Lecture 1"},
            {"payload":'/lecture2{"lecture_type":"lecture2"}', "title": "Lecture 2"},
            {"payload":'/lecture3{"lecture_type":"lecture3"}', "title": "Lecture 3"},
            {"payload":'/lecture4{"lecture_type":"lecture4"}', "title": "Lecture 4"},
            {"payload":'/lecture5{"lecture_type":"lecture5"}', "title": "Lecture 5"},
            {"payload":'/lecture6{"lecture_type":"lecture6"}', "title": "Lecture 6"}
        ]
        dispatcher.utter_message(text="Select the lecture you'd like to know more about", buttons=buttons)

        return []

class action_deliverables(Action):

    def name(self) -> Text:
        return "action_deliverables"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons=[
            {"payload":'/individual{"deliverable_type":"individual"}', "title": "Individual Deliverable"},
            {"payload":'/group{"deliverable_type":"group"}', "title": "Group Deliverable"}
        ]
        dispatcher.utter_message(text="Select a deliverable you'd like to know more about", buttons=buttons)

        return []

class action_individualdeliverables(Action):

    def name(self) -> Text:
        return "action_individualdeliverables"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons=[
            {"payload":'/takeaways{"individualdeliverable_type":"takeaways"}', "title": "Takeaways"},
            {"payload":'/opportunity{"individualdeliverable_type":"opportunity"}', "title": "Opportunity"}
        ]
        dispatcher.utter_message(text="Now select the individual deliverable you'd like to know more about", buttons=buttons)

        return []

class action_takeaways(Action):

    def name(self) -> Text:
        return "action_takeaways"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons=[
            {"payload":'/template{"takeaway_type":"template"}', "title": "Download takeaway template"},
            {"payload":'/submit{"takeaway_type":"submit"}', "title": "Submit takeaway"}
        ]
        dispatcher.utter_message(text="Please choose an action you want to perform", buttons=buttons)

        return []

class action_submittakeaways(Action):

    def name(self) -> Text:
        return "action_submittakeaways"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons=[
            {"payload":'/submittakeaway1{"submittakeaway_type":"submittakeaway1"}', "title": "Module 1. Good AI opportunity"},
            {"payload":'/submittakeaway2{"submittakeaway_type":"submittakeaway2"}', "title": "Module 2. AI STEM"},
            {"payload":'/submittakeaway3{"submittakeaway_type":"submittakeaway3"}', "title": "Module 3. Company Value Creation"},
            {"payload":'/submittakeaway4{"submittakeaway_type":"submittakeaway4"}', "title": "Module 4. City Value Creation"},
            {"payload":'/submittakeaway5{"submittakeaway_type":"submittakeaway5"}', "title": "Module 5. Ecosystems"},
            {"payload":'/submittakeaway6{"submittakeaway_type":"submittakeaway6"}', "title": "Module 6. Investment"}
        ]
        dispatcher.utter_message(text="Select the takeaway you wish to submit", buttons=buttons)

        return []

class action_opportunity(Action):

    def name(self) -> Text:
        return "action_opportunity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons=[
            {"payload":'/guide_opportunity{"opportunity_type":"guide_opportunity"}', "title": "Download opportunity guide"},
            {"payload":'/submit_opportunity{"opportunity_type":"submit_opportunity"}', "title": "Submit opportunity assignment"}
        ]
        dispatcher.utter_message(text="Please choose an action you want to perform", buttons=buttons)

        return []

class action_submitopportunity(Action):

    def name(self) -> Text:
        return "action_submitopportunity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons=[
            {"payload":'/submit_opportunityslide{"submitopportunity_type":"submit_opportunityslide"}', "title": "Slide deck"},
            {"payload":'/submit_opportunityreport{"submitopportunity_type":"submit_opportunityreport"}', "title": "Final Report"}
        ]
        dispatcher.utter_message(text="Select the opportunity deliverable you wish to submit", buttons=buttons)

        return []

class action_groupdeliverable(Action):

    def name(self) -> Text:
        return "action_groupdeliverable"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons=[
            {"payload":'/template_group{"group_type":"template_group"}', "title": "Download AI-Leader template"},
            {"payload":'/submit_group{"group_type":"submit_group"}', "title": "Submit AI-Leader"}
        ]
        dispatcher.utter_message(text="Please choose an action you want to perform", buttons=buttons)

        return []

class action_submitgroup(Action):

    def name(self) -> Text:
        return "action_submitgroup"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons=[
            {"payload":'/submit_groupslide{"submitgroup_type":"submit_groupslide"}', "title": "Slide deck"},
            {"payload":'/submit_groupreport{"submitgroup_type":"submit_groupreport"}', "title": "Final Report"}
        ]
        dispatcher.utter_message(text="Select the group deliverable you wish to submit", buttons=buttons)

        return []
