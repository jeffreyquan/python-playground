import re

string_a = "Horror/Thriller/Action"

string_b = "Comedy - Other"

string_c = "Drama: Other"

string_d = "Fantasy & Horror"

pattern = r' - | & |/|: '

mod_string_a = re.sub(pattern, "_", string_a).lower()
print(mod_string_a) # horror_thriller_action

mod_string_b = re.sub(pattern, "_", string_b).lower()
print(mod_string_b) # comedy_other

mod_string_c = re.sub(pattern, "_", string_c).lower()
print(mod_string_c) # drama_other

mod_string_d = re.sub(pattern, "_", string_d).lower()
print(mod_string_d) # fantasy_horror

