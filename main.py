from pyscript import document 


def candidate_checker(e):
    club_members = [
        "sage aguinaldo",
        "andrey santos",
        "michael barrameda",
        "heather son",
        "miel lindaya",
        "cyra cheang"
    ]

    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value

    candidate = f_name + " " + l_name
    member_checker = candidate.lower() in club_members

    messages = (
        f'Sorry {candidate}, your name is not on the list.',
        f'Congratulations {candidate}, you are part of the Social Science Club!'
    )

    document.getElementById('result').innerHTML = messages[member_checker]