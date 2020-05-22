# on new machines run this in the shell so the database is
# populated and the ids match up
# probably have to rewrite the view/url/template so it doesn't depend
# on ids matching

from index.models import *

for i in range(4):
    burn_for_ids = Painting(name='blah')
    burn_for_ids.save()

paintings = {'Ignus': {'name': 'Ignus', 'translation': 'Fire', 'painting': '/images/ignus_fire.jpg'},'inandantia': {'name': 'inandantia', 'translation': 'flood', 'painting': '/images/inandantia_flood.jpg'},'inaudax': {'name': 'inaudax', 'translation': 'cowardice', 'painting': '/images/inaudax_cowardice.jpg'},'intervigilium': {'name': 'intervigilium', 'translation': 'sleep', 'painting': '/images/intervigilium_sleep.jpg'},'iudicium': {'name': 'iudicium', 'translation': 'judgment', 'painting': '/images/iudicium_judgment.jpg'},'venus': {'name': 'venus', 'translation': 'love', 'painting': '/images/venus_love.jpg'},'viator': {'name': 'viator', 'translation': 'messenger', 'painting': '/images/viator_messenger.jpg'},'vigil': {'name': 'vigil', 'translation': 'watchman', 'painting': '/images/vigil_watchman.jpg'},'vividarium': {'name': 'vividarium', 'translation': 'garden', 'painting': '/images/vividarium_garden.jpg'},'xerampelinae': {'name': 'xerampelinae', 'translation': 'red clothes', 'painting': '/images/xerampelinae_red_clothes.jpg'},'xiphias': {'name': 'xiphias', 'translation': 'swordfish', 'painting': '/images/xiphias_swordfish.jpg'},'xystus': {'name': 'xystus', 'translation': 'tree-lined road', 'painting': '/images/xystus_tree-lined_road.jpg'}}

for name, painting_object in paintings.items():
    new_painting = Painting(name=painting_object['name'], translation=painting_object['translation'], viewed=False, painting=painting_object['painting'])
    new_painting.save()





