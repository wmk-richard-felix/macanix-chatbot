from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

import requests
import json
import os

class ActionSubmitResults(Action):
    def name(self) -> Text:
        return "action_submit_results"
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        # confirm_exercise = tracker.get_slot("confirm_exercise")
        # exercise = tracker.get_slot("exercise")
        # sleep = tracker.get_slot("sleep")
        # stress = tracker.get_slot("stress")
        # diet = tracker.get_slot("diet")
        # goal = tracker.get_slot("goal")

        dispatcher.utter_message("Achamos que seu carro tem o problema 📢!")
        return []
