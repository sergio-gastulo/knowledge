import os

def main():
    values = []
    counter = 1

    # Input loop
    while True:
        value = input("nombre ")
        resp = input("Respuesta en caso la haya ")
        comentario = input("Comentario en la calidad de la pregunta en general ")
        if value.lower() == 'done':
            break
        values.append(f'{counter} \t {value} \t {resp} \t {comentario}')
        counter += 1
        
    # Write values to a text file
    filename = r"C:\Users\sgast\tania\forms_obs.txt"
    with open(filename, 'a') as file:
        for value in values:
            file.write(value + '\n')

    print(f"Values have been stored in {filename}.")

    # Open the text file using the default text editor
    os.system(f'start notepad {filename}')

if __name__ == "__main__":
    main()
