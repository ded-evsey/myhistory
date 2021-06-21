from deeppavlov import build_model, configs
model = build_model(configs.squad.squad_ru, download=False)