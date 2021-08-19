from .models import CandidateInfo


def get_from_db():
    data = CandidateInfo.objects.all()
    send_data = json_parser(data)
    return send_data


def clear_from_db():
    data = CandidateInfo.objects.all()
    data.delete()
    send_data = json_parser(data)
    return send_data


def json_parser(data):
    s_data = {}
    profile_data = {}
    for profile in data:
        for fields in vars(profile):
            if not fields.startswith("_"):
                profile_data[fields] = getattr(profile, fields)
        s_data[profile.id] = profile_data.copy()
    return s_data
