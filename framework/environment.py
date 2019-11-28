def after_scenario(context, scenario):
    webapp.refresh_page()

def after_feature(context, scenario):
    webapp.close_page()