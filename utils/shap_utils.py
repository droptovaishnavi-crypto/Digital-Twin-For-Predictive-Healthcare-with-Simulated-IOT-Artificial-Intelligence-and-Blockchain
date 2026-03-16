# backend/utils/shap_utils.py
import shap

def generate_shap_values(explainer, data):
    shap_values = explainer(data)
    feature_contribs = {}
    for i, feature in enumerate(data.columns):
        feature_contribs[feature] = float(shap_values.values[0][i])
    return feature_contribs
