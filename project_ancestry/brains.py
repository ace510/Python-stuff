from jinja2 import (Environment, PackageLoader, select_autoescape, ChoiceLoader, 
FileSystemLoader, ModuleLoader)
import os, logging



def initialize():
       """ initialize the Jinja Loader and environment """
       jinja_loader=ChoiceLoader([
              ModuleLoader(".\\compiled_templates"),
              FileSystemLoader(".\\templates")
       ])
       env = Environment(loader=jinja_loader,
              autoescape=select_autoescape(['html', 'xml'])
              )

       return env


def publish(template_name, publish_name, env, contents, contents_2):
       output_folder ='.\\.output\\'
       """ render the jinja templates, push to output directory """
       
       output_file = output_folder + str(publish_name)
       template = env.get_template(template_name)
       im_so_random = template.render(words = contents, title = contents_2)
       
       with open(output_file, 'w') as future_web_site:
              for line in im_so_random:
                     future_web_site.write(line)

       print('website complete, check it out')

def namify(item_name: str) -> str:
    output = '.\\' + item_name + '.html'

    return output

def directory_waltz(input_home :str , jinja_env):
       """Gets all of the pictures and their catagories in order to pass them
       to rendering"""
       CRANKEN_WALTZ = os.walk(input_home)

       eins :str = next(CRANKEN_WALTZ)
       logging.debug(f'the first element of the directory walk is {eins}')

       # mit dem os.walk, der tuple is 
       # directory path, name of sub directories, names of files
       for Fuss in CRANKEN_WALTZ:
              # this grabs the folder name (to be the title of the page)
              # as well as all the pictures, then makes paths out of the two
              # then adds them to a set to iterate through
              index_dict = dict()
              category_name = Fuss[0].split('\\')[-1]
              index_path =  namify(category_name)
              logging.debug(index_path)
              index_dict[category_name] = index_path
              
              category_file_name = category_name + '.html'
              sub_files = Fuss[2]
              sub_file_paths = set()
              test_input_path = 'C:\\valley_forge\\Python-stuff\\project_ancestry\\.input'

              for file in sub_files:
                     sub_file_path = os.path.join(test_input_path, category_name, file)
                     sub_file_paths.add(sub_file_path)
              publish('pic_list.html', category_file_name,
              jinja_env, sub_file_paths, category_name)

       return index_dict


def main():
    logging.basicConfig(level=logging.DEBUG)
    pic_input_file = '.input'
    words = ('deez', 'nuts', 'drive', 'fast', 'eat', 'ass', 'hail', 'satan')
    images = ('https://picsum.photos/200','https://picsum.photos/300',
    'https://picsum.photos/400','https://picsum.photos/500',
    'https://picsum.photos/500','https://picsum.photos/200')
    
    jinja_env = initialize()

    publish('word_list.html', 'words.html',  jinja_env, words, 'Massive Chungus')
    publish('pic_list.html', 'pics.html',   jinja_env, images, 'Memes')
    index_dict = directory_waltz(pic_input_file,jinja_env)

    publish('index.html', 'index.html', jinja_env, index_dict, 'Index')

if __name__ == "__main__":
    main()