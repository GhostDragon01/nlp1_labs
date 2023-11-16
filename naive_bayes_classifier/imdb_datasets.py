from datasets import load_dataset_builder
ds_builder = load_dataset_builder("imdb")
print(ds_builder.info.description)
print(ds_builder.info.features)