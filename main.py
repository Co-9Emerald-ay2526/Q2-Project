# 2nd Quarter Project
from pyscript import display, document


def result_checker(e):
    document.getElementById('output').innerHTML = " "
    # Member sets by grade level
    grade7 = {'LeBron James', 'Bronny James', 'Bryce James'}
    grade8 = {'Spongebob Squarepants', 'Squidward Tentacles', 'Eugene Krabs', 'Sandy Cheeks'}
    grade9 = {'Greg Heffley', 'Rowley Jefferson', 'Chirag Gupta'}
    grade10 = {'Peter Parker', 'Michelle Jones', 'Ned Leeds', 'Flash Thompson'}
    # Get user input and create new member
    first_name = document.getElementById('first_name').value
    last_name = document.getElementById('last_name').value
    new_members = first_name + " " + last_name
    new_members_set = {new_members}        
    all_members = grade7 | grade8 | grade9 | grade10 | new_members_set
    total_members = len(all_members)
    # Display member list and total count in HTML
    members_list = "<br>".join(sorted(all_members))
    document.getElementById('output').innerHTML = f'All members:<br>  {members_list}'
    display(f'Total members: {total_members}', target='output')

# Skills Test
from pyscript import display, document

nonmetals = {
    "H":  ("Hydrogen",    1,   1.008),
    "B":  ("Boron",       5,   10.81),
    "N":  ("Nitrogen",    7,   14.007),
    "O":  ("Oxygen",      8,   15.999),
    "Ne": ("Neon",       10,   20.180),
    "Si": ("Silicon",    14,   28.085),
    "P":  ("Phosphorus", 15,   30.974),
    "S":  ("Sulfur",    16,   32.06),
    "Cl": ("Chlorine",  17,   35.45),
    "As": ("Arsenic",   33,   74.922),
    "Br": ("Bromine",   35,   79.904),
    "Te": ("Tellurium", 52,   127.60),
    "I":  ("Iodine",    53,   126.90),
    "Xe": ("Xenon",     54,   131.29),
    "At": ("Astatine",  85,   210),
    "Rn": ("Radon",    86,   222)
}

def element_checker(e):
    document.getElementById('result').innerHTML = " "
    element1 = document.getElementById('element_name').value.strip().title()
    result = nonmetals.get( element1, ("Element not found", "N/A", "N/a"))
    
    document.getElementById('result').innerHTML = f"""
    <b>Symbol:</b> {element1}<br>
    <b>Element:</b> {result[0]}<br>
    <b>Atomic Number:</b> {result[1]}<br>
    <b>Atomic Mass:</b> {result[2]}
    """
