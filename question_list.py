import requests
parameters = {
    "amount": 10,
    'type': "boolean"
}
response = requests.get("https://opentdb.com/api.php", params= parameters)
response.raise_for_status()
question_list = response.json()["results"]



# question_list =[
#     {
#         "category":"General Knowledge",
#         "type":"boolean","difficulty":"easy",
#         "question":"Bulls are attracted to the color red.",
#         "correct_answer":"False",
#         "incorrect_answers":["True"]
#         },
#     {"category":"Entertainment: Video Games","type":"boolean","difficulty":"medium","question":"In Half-Life 2, if you play the zombies&#039; speech in reverse, they actually speak coherent English.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Geography","type":"boolean","difficulty":"easy","question":"There are no deserts in Europe.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Entertainment: Comics","type":"boolean","difficulty":"medium","question":"In the webcomic Homestuck, the first character introduced is Dave Strider.","correct_answer":"False","incorrect_answers":["True"]},{"category":"General Knowledge","type":"boolean","difficulty":"easy","question":"Pluto is a planet.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Vehicles","type":"boolean","difficulty":"medium","question":"The General Motors EV1 was the first street-legal production electric vehicle.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Entertainment: Film","type":"boolean","difficulty":"easy","question":"George Lucas directed the entire original Star Wars trilogy.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Entertainment: Video Games","type":"boolean","difficulty":"easy","question":"In RuneScape, one must complete the &quot;Dragon Slayer&quot; quest before equipping Rune Platelegs.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Entertainment: Video Games","type":"boolean","difficulty":"easy","question":"The ghosts in &quot;Pac-Man&quot; and &quot;Ms. Pac-Man&quot; have completely different behavior.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Science & Nature","type":"boolean","difficulty":"medium","question":"Sound can travel through a vacuum.","correct_answer":"False","incorrect_answers":["True"]}]