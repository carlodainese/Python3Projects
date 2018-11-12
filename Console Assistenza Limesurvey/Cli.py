"""
Sessions
get_session_key (api.open)
release_session_key (api.close)

Survey
list_surveys
list_questions

Token
add_participants
delete_participants
get_participant_properties
get_summary
invite_participants
list_participants

"""


from limesurveyrc2api.limesurvey import LimeSurvey
from limesurveyrc2api.exceptions import LimeSurveyError
from limesurveyrc2api._survey import _Survey
from limesurveyrc2api._token import _Token

url = "https://qpidsv.intra.infocamere.it/index.php/admin/remotecontrol"
username = "admin"
password = "password"

# Open a session.
api = LimeSurvey(url=url, username=username)
api.open(password=password)

# Get a list of surveys the admin can see, and print their IDs.
result = api.survey.list_surveys()
#for survey in result:
#    print(survey.get("sid"))

# get data from survey # 531223
id_survey = 531223
token = _Token(api)
#search for email
email_target = "carlo.dainese@infocamere.it"
tid = ""
part_start = 0
part_limit = 999999
partecipanti = token.list_participants(id_survey,part_start,part_limit)
for persona in partecipanti:
    #print(persona)
    if (email_target == persona.get("participant_info").get("email")):
        tok =  persona.get("token")
        tid = persona.get("tid")
        print("found it! " + str(tok))
        break
#send invitation
list=[]
list.append(tid);
token.invite_participants(id_survey, list, False);

# Close the session.
api.close()

