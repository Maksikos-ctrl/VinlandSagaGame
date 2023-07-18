


from csv import reader as rd
from os import walk
import pygame





def import_csv_layout(path):
    terrain = []
    with open(path, 'r') as f:
        layout = rd(f, delimiter=',')

        for row in layout:
            terrain.append(list(row))


        return terrain    

       
def import_folder(path):
       
    surface_list = []


    # _ = means we don't care about the first value(we don't need it)
    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surface)


    return surface_list        

        
        
        

    
print(import_folder('../assets/grass'))