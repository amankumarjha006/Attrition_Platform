from attrition_ml.model_loader import (
    get_model,
    get_preprocessor,
    get_feature_names,
    get_metadata,
)

print(type(get_model()))
print(type(get_preprocessor()))
print(len(get_feature_names()))
print(get_metadata())