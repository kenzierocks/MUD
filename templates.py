__author__ = 'Kenzie Togami'
import os
import sys
import traceback
exist = os.path.exists

template_dir = 'data/templates'
if not exist(template_dir):
    os.mkdir(template_dir)
templates = []
sys.path.append(template_dir)
for templ in os.listdir(template_dir):
    if not templ.endswith('.py'):
        continue
    try:
        mod = __import__(templ[:-3])
        templ_ref = mod.instance  # loads the template instance
    except:
        print("Couldn't load template reference", templ)
        traceback.print_exc()
        continue
    templates.append(templ_ref)


def find_template(site):
    for template in templates:
        if template.will_process(site):
            return template
    raise ValueError("no template for {}".format(site))
