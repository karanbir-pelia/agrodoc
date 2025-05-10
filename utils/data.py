# Contains data structures like class names and remedial measures

def get_class_names_by_plant():
    """Returns a dictionary mapping plant names to their possible conditions."""
    return {
        'Apple': ['Apple Scab',
                  'Black Rot',
                  'Cedar Apple Rust',
                  'Healthy'],
        'Bell Pepper': ['Bacterial Spot',
                        'Healthy'],
        'Blueberry': ['Healthy'],
        'Cherry': ['Healthy',
                  'Powdery Mildew'],
        'Corn': ['Cercospora Leaf Spot (Gray Leaf Spot)',
                 'Common Rust',
                 'Northern Leaf Blight',
                 'Healthy'],
        'Grape': ['Black Rot',
                  'Esca (Black Measles)',
                  'Leaf Blight (Isariopsis Leaf Spot)',
                  'Healthy'],
        'Orange': ['Huanglongbing (Citrus Greening)'],
        'Peach': ['Bacterial Spot',
                  'Healthy'],
        'Potato': ['Early Blight',
                   'Late Blight',
                   'Healthy'],
        'Raspberry': ['Healthy'],
        'Soybean': ['Healthy'],
        'Squash': ['Powdery Mildew'],
        'Strawberry': ['Leaf Scorch',
                       'Healthy'],
        'Tomato': ['Bacterial Spot',
                   'Early Blight',
                   'Late Blight',
                   'Leaf Mold',
                   'Septoria Leaf Spot',
                   'Spider Mites',
                   'Target Spot',
                   'Tomato Yellow Leaf Curl Virus',
                   'Tomato Mosaic Virus',
                   'Healthy']
    }

def get_model_class_names():
    """Returns a tuple of (plant, condition) tuples for model prediction."""
    return (
        ('Apple', 'Apple Scab'),
        ('Apple', 'Black Rot'),
        ('Apple', 'Cedar Apple Rust'),
        ('Apple', 'Healthy'),
        ('Blueberry', 'Healthy'),
        ('Cherry', 'Powdery Mildew'),
        ('Cherry', 'Healthy'),
        ('Corn', 'Cercospora Leaf Spot Gray Leaf Spot'),
        ('Corn', 'Common Rust'),
        ('Corn', 'Northern Leaf Blight'),
        ('Corn', 'Healthy'),
        ('Grape', 'Black Rot'),
        ('Grape', 'Esca (Black Measles)'),
        ('Grape', 'Leaf Blight (Isariopsis Leaf Spot)'),
        ('Grape', 'Healthy'),
        ('Orange', 'Huanglongbing (Citrus Greening)'),
        ('Peach', 'Bacterial Spot'),
        ('Peach', 'Healthy'),
        ('Bell Pepper', 'Bacterial Spot'),
        ('Bell Pepper', 'Healthy'),
        ('Potato', 'Early Blight'),
        ('Potato', 'Late Blight'),
        ('Potato', 'Healthy'),
        ('Raspberry', 'Healthy'),
        ('Soybean', 'Healthy'),
        ('Squash', 'Powdery Mildew'),
        ('Strawberry', 'Leaf Scorch'),
        ('Strawberry', 'Healthy'),
        ('Tomato', 'Bacterial Spot'),
        ('Tomato', 'Early Blight'),
        ('Tomato', 'Late Blight'),
        ('Tomato', 'Leaf Mold'),
        ('Tomato', 'Septoria Leaf Spot'),
        ('Tomato', 'Spider Mites'),
        ('Tomato', 'Target Spot'),
        ('Tomato', 'Tomato Yellow Leaf Curl Virus'),
        ('Tomato', 'Tomato Mosaic Virus'),
        ('Tomato', 'Healthy')
    )

def get_remedial_measures():
    """Returns a dictionary mapping plants and conditions to remedial measures."""
    return {
        'Apple': {
            'Apple Scab':
    '''
Remedial Actions:
- Prune and remove infected leaves, fruit, and branches.

- Apply fungicidal sprays containing captan, mancozeb, or sulfur.

- Implement cultural practices like mulching, avoiding overhead irrigation, thinning fruit clusters, and removing fallen leaves and fruit.''',
            'Black Rot':
    '''
Remedial Actions:
- Remove and destroy infected fruit and plant material.

- Apply fungicidal sprays containing captan or thiophanate-methyl.

- Implement cultural practices like pruning, spacing, and avoiding overhead irrigation.''',
            'Cedar Apple Rust':
    '''
Remedial Actions:
- Prune infected branches.

- Apply fungicidal sprays with myclobutanil or thiophanate-methyl.

- Implement cultural practices: plant resistant apple varieties, remove nearby cedar trees, and ensure good air circulation.''',
            'Healthy':"",
            },
        'Bell Pepper': {
            'Bacterial Spot':
    '''
Remedial Actions:
- Remove infected plant debris.

- Apply copper-based bactericides.

- Practice crop rotation and choose resistant varieties.''',
            'Healthy':"",
            },
        'Blueberry': {
            'Healthy':"",
            },
        'Cherry': {
            'Healthy':"",
            'Powdery Mildew':
    '''
Remedial Actions:
- Apply fungicidal sprays containing sulfur or potassium bicarbonate.

- Prune trees to improve air circulation.

- Implement cultural practices like watering at the base and removing fallen leaves.''',
            },
        'Corn': {
            'Cercospora Leaf Spot (Gray Leaf Spot)':
    '''
Remedial Actions:
- Apply fungicidal sprays with azoxystrobin or pyraclostrobin.

- Practice crop rotation and manage crop residue.

- Implement cultural practices like planting resistant varieties and spacing plants properly.''',
            'Common Rust':
    '''
Remedial Actions:
- Apply fungicidal sprays containing triazoles or strobilurins.

- Practice crop rotation and manage crop residue.

- Implement cultural practices like planting resistant varieties and spacing plants properly.''',
            'Northern Leaf Blight':
    '''
Remedial Actions:
- Apply fungicidal sprays with triazoles or strobilurins.

- Practice crop rotation and manage residue.

- Implement cultural practices like planting resistant varieties and proper spacing.''',
            'Healthy':"",
            },
        'Grape': {
            'Black Rot':
    '''
Remedial Actions:
- Remove infected grape clusters and debris.

- Apply fungicidal sprays with captan, mancozeb, or azoxystrobin.

- Implement cultural practices like pruning for air circulation and proper vineyard floor management.''',
            'Esca (Black Measles)':
    '''
Remedial Actions:
- Prune infected vines and promptly remove symptomatic shoots.

- Apply fungicides with fosetyl-aluminum or propiconazole preventatively.

- Protect vine wounds with sealants after pruning.''',
            'Leaf Blight (Isariopsis Leaf Spot)':
    '''
Remedial Actions:
- Apply fungicidal sprays with azoxystrobin, trifloxystrobin, or tebuconazole.

- Implement cultural practices like proper vine spacing and selective leaf removal.

- Remove and destroy infected leaves and clusters.''',
            'Healthy':"",
            },
        'Orange': {
            'Huanglongbing (Citrus Greening)':
    '''
Remedial Actions:
- Control the Asian citrus psyllid vector.

- Promote tree health through proper nutrition and care.

- Consider thermotherapy and antibiotic treatments for infected trees''',
            },
        'Peach': {
            'Bacterial Spot':
    '''
Remedial Actions:
- Apply copper-based bactericides preventatively.

- Prune and remove infected branches and plant material.

- Implement cultural practices like avoiding overhead irrigation and promoting good air circulation.''',
            'Healthy':"",
            },
        'Potato': {
            'Early Blight':
    '''
Remedial Actions:
- Apply fungicides with chlorothalonil or mancozeb.

- Practice crop rotation and manage residue.

- Implement cultural practices like planting resistant varieties and proper spacing.''',
            'Late Blight':
    '''
Remedial Actions:
- Apply fungicides with chlorothalonil, mancozeb, or metalaxyl.

- Implement cultural practices like planting resistant varieties and proper spacing.

- Regularly scout fields for early detection and remove infected plants.''',
            'Healthy':"",
            },
        'Raspberry': {
            'Healthy':"",
            },
        'Soybean': {
            'Healthy':"",
            },
        'Squash': {
            'Powdery Mildew':
    '''
Remedial Actions:
- Apply fungicides with sulfur, potassium bicarbonate, or neem oil.

- Implement cultural practices like proper spacing and removing infected debris.

- Consider planting resistant squash varieties.''',
            },
        'Strawberry': {
            'Leaf Scorch':
    '''
Remedial Actions:
- Remove and destroy infected plants.

- Apply fungicides with azoxystrobin or myclobutanil.

- Implement cultural practices like planting resistant varieties and proper spacing.''',
            'Healthy':"",
            },
        'Tomato': {
            'Bacterial Spot':
    '''
Remedial Actions:
- Remove and destroy infected plant material.

- Apply copper-based bactericides preventatively.

- Implement cultural practices like proper spacing and avoiding overhead irrigation.''',
            'Early Blight':
    '''
Remedial Actions:
- Remove infected plant material.

- Apply fungicides with chlorothalonil or mancozeb preventatively.

- Implement cultural practices like proper spacing and mulching.''',
            'Late Blight':
    '''
Remedial Actions:
- Remove infected plant material.

- Apply fungicides with chlorothalonil or mancozeb preventatively.

- Implement cultural practices like proper spacing and avoiding overhead irrigation.''',
            'Leaf Mold':
    '''
Remedial Actions:
- Apply fungicides with chlorothalonil or copper-based products preventatively.

- Increase spacing between plants to improve air circulation.

- Avoid overhead irrigation and water at the base of plants.''',
            'Septoria Leaf Spot':
    '''
Remedial Actions:
- Apply chlorothalonil or copper-based fungicides preventatively.

- Prune infected lower leaves and ensure good airflow.

- Mulch around plants and water at the base to prevent soil splash and reduce humidity.''',
            'Spider Mites':
    '''
Remedial Actions:
- Spray with insecticidal soap or neem oil.

- Introduce natural predators like ladybugs.

- Implement cultural practices like spraying with water and maintaining proper plant spacing.''',
            'Target Spot':
    '''
Remedial Actions:
- Apply fungicides with chlorothalonil or mancozeb preventatively.

- Prune and remove infected plant material for sanitation.

- Water at the base of plants and avoid overhead irrigation.''',
            'Tomato Yellow Leaf Curl Virus':
    '''
Remedial Actions:
- Plant resistant tomato varieties.

- Control whitefly vectors through insecticides or physical barriers.

- Rotate crops and remove infected plants promptly.''',
            'Tomato Mosaic Virus':
    '''
Remedial Actions:
- Start with certified virus-free seeds.

- Control aphid vectors with insecticides or barriers.

- Remove and destroy infected plants promptly.''',
            'Healthy':"",
            },
        }