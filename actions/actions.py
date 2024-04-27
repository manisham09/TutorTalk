# This files contains your custom actions which can be used to run
# custom Python code.
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_servicebc"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        prompt=next(tracker.get_latest_entity_values('service based company'),None)
        if prompt:
            dispatcher.utter_message(text="1.Registration\n"
                                          "2.Resume Shortlisting(It can be done on any based mentioned in the resume)\n"
                                          "3.Online Assessment\n"
                                          "\tThis test includes:\n"
                                          "\t\tApti Test:\n"
                                          "\t\t\tQuants\n"
                                          "\t\t\tLogical Reasoning\n"
                                          "\t\t\tVerbal Reasoning\n"
                                          "\t\t\tData Interpretation\n"
                                          "\t\t\tPsychometric Test\n"
                                          "\t\t\tGame Based Apti\n"
                                          "\t\t\tVisual Reasoning\n"
                                          "\t\t\tCoding\n"
                                          "\t\t\tProgramming MCQ(C/C++)\n"
                                          "\t\t\tDSA(Intermediate)\n"
                                          "\t\t\tMCQ’s on SQL,DBMS,CN,OS\n"
                                          "\t=> for product based companies: Additionally need to build up good coding skills\n"
                                          "4.For some roles in service based companies they have Additional Advanced Coding Test\n"
                                          "5.5.	Technical Interview\n"
                                          "\t1. C++/java/python(Make sure to learn atleast one language thoroughly)\n"
                                          "\t2. Puzzles\n"
                                          "\t3. Discussion on Projects(that can be demonstrated by sharing screen)\n"
                                          "\t4. DSA(Intermediate)Here they may ask you to write the code, explain the logic, etc.\n"
                                          "\t5. Interviewer may ask about the behavioural questions, and they can also ask about the things mentioned in the resume\n"
                                           "Some companies may have additionally one more technical round\n"
                                          "6.HR Interview\n"
                                          "\t1. Situation Based Questions\n"
                                          "\t2. Stress Based Questions\n"
                                          "\t3. Discussion on projects\n"
                                          "\t4. Business Ethics\n"
                                          "\t5. Corporate Ethics\n"
                                          "\t6. Behavioural Questions\n"
                                          "7.Familiarize with the STAR(Situation, Task, Action, Result) method for answering behavioral interview Questions.\n"
                                          "Don't lie to the interviewers\n"
                                          "8.Selection / Rejection\n"
                                          "9.Offer Rollout\n"
            )
        else:
            prompt1=next(tracker.get_latest_entity_values('competitive coder'),None)
            if prompt1:
                dispatcher.utter_message(text="1.Pick up a programming language usually c++ or java or python preferred because they are support object oriented\n"
                                        "\tPlatforms:\n"
                                        "\t\t1. HackerRank\n"
                                        "\t\t2. GeeksforGeeks\n"
                                        "\t\t3.JavaTpoint\n"
                                        "\t\t4. InfosysSpringBoard\n"
                                        "\t\t5. Swayam NPTEL\n"
                                        "2.Learn Data Structure and Algorithms(Basic & Advanced)\n"
                                        "3.Start Practicing and solving problems\n"
                                        "\tCoding platforms:\n"
                                        "\t\t1. Codechef\n"
                                        "\t\t2. Leetcode\n"
                                        "\t\t3. Codeforces\n"
                                        "\t\t4. GeeksforGeeks\n"
                                        "\t\t5. InterviewBit(For intermediate & Advanced level)\n"
                                        "4.Start participating in coding challenges or contests\n"
                                        "small tip: once the coding contest ends, practice the contest problems which are not done during contest\n"
                                        "\tplatforms:\n"
                                        "\t\tCodechef\n"
                                        "\t\tLeetcode\n"
                                        "\t\tcodeforces\n" 
                                        "\n(To know about the resources like tutorials or courses need to be taken ask for resources)"
                                        "5.Finally, Staying consistent is more important to become a master in competitive programming\n"
                )
            else:
                prompt2 = next(tracker.get_latest_entity_values('resources for competitive programming'), None)
                if prompt2:
                    dispatcher.utter_message(text="Some suggested Youtube Tutorials are:\n"
                    "\t1.Tushar Roy\n"
                    "\t2.Apna college\n"
                    "\t3.take U forward\n"
                    "\t4.WilliamFiset\n"
                    "\t5.Aditya Verma\n"
                    "\t6.Pepcoding\n"
                    "\t7.Code NCode\n"
                    "\t8.Gaurav Sen\n"
                    "\t9.Rachit Jain\n"
                    "\t10.code_report\n"
                    "\t11.Abdul Bari\n")
                else:
                    dispatcher.utter_message(text="sorry i did'nt get you")
        return []
