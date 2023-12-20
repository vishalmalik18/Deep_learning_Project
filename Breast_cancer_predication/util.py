from keras.models import load_model

__model = None

def load_saved_artificats():
    print("loading saved artifacts...start")
    
    global __model
    if __model is None:
        model_path = "C:/Users/visha/OneDrive/Desktop/Breast_cancer_predication/breast_cancer_Predication_model.h5"
        __model = load_model(model_path)

def breast_cancer_predication(radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, 
           concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se,
           texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, 
           concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, 
           perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, 
           concave_points_worst, symmetry_worst, fractal_dimension_worst):
    
    prediction = __model.predict([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, 
                                 compactness_mean, concavity_mean, concave_points_mean, symmetry_mean,
                                 fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se,
                                 smoothness_se, compactness_se, concavity_se, concave_points_se,
                                 symmetry_se, fractal_dimension_se, radius_worst, texture_worst,
                                 perimeter_worst, area_worst, smoothness_worst, compactness_worst,
                                 concavity_worst, concave_points_worst, symmetry_worst,
                                 fractal_dimension_worst]])
    # print(type(prediction))
    # if prediction > 0.5:
    #     return "You are M vairent painent"
    # else:
    #     return "You are B vairent Painetnt"
    return prediction


if __name__ == '__main__':
    load_saved_artificats()
    print(breast_cancer_predication(radius_mean=17.99, texture_mean=10.38, perimeter_mean=122.8, area_mean=1001, smoothness_mean=0.1184,
        compactness_mean=0.2776, concavity_mean=0.3001,concave_points_mean=0.1471, symmetry_mean=0.2419, 
        fractal_dimension_mean=0.07871, radius_se=1.095, texture_se=0.9053, perimeter_se=8.589,
        area_se=153.4, smoothness_se=0.006399, compactness_se=0.04904, concavity_se=0.05373, 
        concave_points_se=0.01587, symmetry_se=0.03003, fractal_dimension_se=0.006193, 
        radius_worst=25.38, texture_worst=17.33, perimeter_worst=184.6, area_worst=2019,
        smoothness_worst=0.1622, compactness_worst=0.6656, concavity_worst=0.7119,
        concave_points_worst=0.2654, symmetry_worst=0.4601, fractal_dimension_worst=0.1189))