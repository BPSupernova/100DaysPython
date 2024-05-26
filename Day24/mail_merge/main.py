letter_template = ""
invitees = []
with open("C:/Users/Ben/100DaysPython/Day24/mail_merge/Input/Letters/starting_letter.txt") as letter:
    letter_template += letter.read()

with open("C:/Users/Ben/100DaysPython/Day24/mail_merge/Input/Names/invited_names.txt") as names_list:
    invitees = names_list.readlines()

def remove_new_line_sequence(string):
    return string[0 : len(string) - 1]

for num_person in range(0, len(invitees)):
    reformatted_name = remove_new_line_sequence(invitees[num_person])
    reformatted_name = reformatted_name.strip()
    invitees[num_person] = reformatted_name
    with open(f"{invitees[num_person]}_invitation.txt", mode="w") as personalized_letter:
        personalized_letter.write(letter_template.replace("[name]", invitees[num_person]))

