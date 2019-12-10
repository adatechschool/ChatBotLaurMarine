from chatterbot import ChatBot

bot = ChatBot(
	"NaiveBot", #Nom

storage_adapter="chatterbot.adapters.storage.JsonFileStorageAdapter"
,
	input_adapter="chatterbot.adapters.input.TerminalAdapter",
	output_adapter="chatterbot.adapters.output.TerminalAdapter",
	# Désactiver le logic_adapters pour le learning
	logic_adapters=["chatterbot.adapters.logic.ClosestMatchAdapter",
],
	database="naive_database.db", #nom de la base d'échanges
	silence_performance_warning=True
)

while True:
	try:
		bot_input = bot.get_response(None)
	except(KeyboardInterrupt, EOFError, SystemExit):
		break
