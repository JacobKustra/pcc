unprinted_models = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_models:
    current_design = unprinted_models.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

print("\nThe following models have been printed:")
for model in completed_models:
    print(model)


print("\n\nRestructured")
def print_models(unprinted_models, completed_models):
    while unprinted_models:
        current_design = unprinted_models.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(model)

unprinted_models = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_models, completed_models)
show_completed_models(completed_models)


print("Save original lists")
unprinted_models = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_models[:], completed_models)
show_completed_models(completed_models)
print(unprinted_models)
