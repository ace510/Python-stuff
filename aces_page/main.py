from jinja2 import (
    Environment,
    PackageLoader,
    select_autoescape,
    ChoiceLoader,
    FileSystemLoader,
    ModuleLoader,
)
import os


def publish(template_name, publish_name, env, contents, contents_2):
    output_folder = "C:\\valley_forge\\ace510.github.io\\"
    """ render the jinja templates, push to output directory """

    output_file = output_folder + str(publish_name)
    print("output file is:")
    print(output_file)
    template = env.get_template(template_name)
    im_so_random = template.render(words=contents, title=contents_2)

    with open(output_file, "w") as future_web_site:
        for line in im_so_random:
            future_web_site.write(line)

    print("website complete, check it out")


def initialize():
    """ initialize the Jinja Loader and environment """
    jinja_loader = ChoiceLoader(
        [ModuleLoader(".\\compiled_templates"), FileSystemLoader(".\\templates")]
    )
    env = Environment(
        loader=jinja_loader, autoescape=select_autoescape(["html", "xml"])
    )

    return env


def main():

    jinja_env = initialize()

    publish("index.html", "index.html", jinja_env, "lard", "Ace's Page")
    publish("projects.html", "projects.html", jinja_env, "lard", "Projects")


if __name__ == "__main__":
    main()
