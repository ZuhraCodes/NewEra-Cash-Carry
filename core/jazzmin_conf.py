JAZZMIN_SETTINGS: dict = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "NewEra Chash&Carry Admin",
    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "NewEra Chash&Carry Admin",
    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "NewEra Chash&Carry Admin",
    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "img/image.png",
    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": "img/image.png",
    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": None,
    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-square",
    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,
    # Welcome text on the login screen
    "welcome_sign": "NewEra Chash&Carry Admin",
    # Copyright on the footer
    "copyright": "NewEra Chash&Carry",
    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "",
    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {
            "name": "Home",
            "url": "admin:index",
            "permissions": ["auth.view_user"],
        },
        # external url that opens in a new window (Permissions can be added)
        # {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
    ],
    #############
    # User Menu #
    #############
    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [{"model": "auth.user"}],
    #############
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": False,
    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],
    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],
    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": [
        # "common.Region",
    ],
    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        #
        "auth": "fas fa-users-cog",
        "auth.User": "fas fa-duotone fa-user-tie",
        "auth.Group": "fas fa-duotone fa-users",
        # #
        # "news": "fas fa-calendar-alt",
        # "news.News": "fas fa-square-full-white",
        # "news.Event": "fa fa-square-full-white",
        # "news.Region": "fa fa-square-full-white",
        # "news.Newstag": "fas fa-square-full-white",
        # "news.EventCategory": "fa fa-square-full-white",
        # "news.NewsCategory": "fas fa-square-full-white",
        #
        # "document.DocumentCategory": "fas fa-square-full-white",
        # "document.Document": "fas fa-square-full-white",
        # "document.StateStandard": "fas fa-square-full-white",
        #
        # "recommendation.FAQ": "fas fa-square-full-white",
        # "recommendation.Application": "fas fa-square-full-white",
        # "recommendation.DownloadPrograms": "fas fa-square-full-white",
        # "recommendation.NetworkMonitoring": "fas fa-square-full-white",
        # "recommendation.FAQTag": "fas fa-square-full-white",
        #
        # "common": "fas fa-info",
        # "common.Statistic": "fas fa-square-full-white",
        # "common.Slider": "fas fa-square-full-white",
        # "common.SourcesAndSponsors": "fas fa-square-full-white",
        # "common.AboutUs": "fas fa-square-full-white",
        # "common.Hack": "fas fa-square-full-white",
        # "common.Source": "fas fa-square-full-white",
        # "common.Partner": "fas fa-square-full-white",
        # "common.Application": "fas fa-square-full-white",
        # "common.HeaderMenu": "fas fa-square-full-white",
        # "common.FooterMenu": "fas fa-square-full-white",
        # "common.MainMenu": "fas fa-square-full-white",
        # "common.Pages": "fas fa-square-full-white",
        # "common.FAQTag": "fas fa-square-full-white",
        # "common.FAQ": "fas fa-square-full-white",
        # "common.Contact": "fas fa-square-full-white",
        # "common.ContactUser": "fas fa-square-full-white",
        # "common.Feedback": "fas fa-square-full-white",
        # "common.Country": "fas fa-square-full-white",
        #
        # "aboutus": "fas fa-eject",
        # "aboutus.Header": "fas fa-square-full-white",
        # "aboutus.WhatWeDo": "fas fa-square-full-white",
        # "aboutus.AboutCenterHistory": "fas fa-square-full-white",
        # "aboutus.AboutCenterGoal": "fas fa-square-full-white",
        # "aboutus.Statistic": "fas fa-square-full-white",
        # "aboutus.Management": "fas fa-square-full-white",
        # "aboutus.Representative": "fas fa-square-full-white",
        # "aboutus.MainMenu": "fas fa-square-full-white",
        # "aboutus.CenterStructure": "fas fa-square-full-white",
        # "aboutus.Country": "fas fa-square-full-white",
        # "aboutus.Department": "fas fa-square-full-white",
        # "aboutus.Vacancy": "fas fa-square-full-white",
        # "aboutus.ResumeApplication": "fas fa-square-full-white",
        # "aboutus.StaticPage": "fas fa-square-full-white",
        #
        # "main": "fas fa-home",
        # "main.Slider": "fas fa-square-full-white",
        # "main.PayStatistic": "fas fa-square-full-white",
        # "main.BannerMenu": "fas fa-square-full-white",
        # "main.HeaderMenu": "fas fa-square-full-white",
        # "main.Source": "fas fa-square-full-white",
        # "main.Quote": "fas fa-square-full-white",
        # "main.FooterMenu": "fas fa-square-full-white",
        # "main.CharityProject": "fas fa-square-full-white",
        # "main.NewsletterEmail": "fas fa-square-full-white",
        # "main.InstagramPhoto": "fas fa-square-full-white",
        # "main.UsefulLink": "fas fa-square-full-white",
        # #
        # "projects": "fas fa-lightbulb",
        # "projects.Project": "fas fa-square-full-white",
        # "projects.Introduction": "fas fa-square-full-white",
        # "projects.AboutProject": "fas fa-square-full-white",
        # "projects.GoalAndMission": "fas fa-square-full-white",
        # "projects.Document": "fas fa-square-full-white",
        # "projects.ProjectDocument": "fas fa-square-full-white",
        # "projects.TeamMember": "fas fa-square-full-white",
        # "projects.Feedback": "fas fa-square-full-white",
        #
    #     "services": "fas fa-bolt",
    #     "services.ServiceCategory": "fas fa-square-full-white",
    #     "services.CareerAbout": "fas fa-square-full-white",
    #     "services.YoungInnovator": "fas fa-square-full-white",
    #     "services.PhotoGallery": "fas fa-square-full-white",
    #     "services.GratuitousHelp": "fas fa-square-full-white",
    #     "services.MigrationLaw": "fas fa-square-full-white",
    #     "services.Insurance": "fas fa-square-full-white",
    #     "services.CountryLaw": "fas fa-square-full-white",
    #     "services.Obligations": "fas fa-square-full-white",
    #     "services.LibraryCatalog": "fas fa-square-full-white",
    #     "services.Book": "fas fa-square-full-white",
    #     "services.LegalLabAbout": "fas fa-square-full-white",
    #     "services.Support": "fas fa-square-full-white",
    #     "services.OrganizationsCategory": "fas fa-square-full-white",
    #     "services.Embassy": "fas fa-square-full-white",
    #     "services.PartnersCategory": "fas fa-square-full-white",
    #     "services.Partnership": "fas fa-square-full-white",
    #     "services.PartnerOrganization": "fas fa-square-full-white",
    #     "services.ForVolunteer": "fas fa-square-full-white",
    #     "services.VolunteerResume": "fas fa-square-full-white",
    #     "services.Volunteer": "fas fa-square-full-white",
    #     "services.Coordinator": "fas fa-square-full-white",
    #     "services.Opportunity": "fas fa-square-full-white",
    },
    # # Icons that are used when one is not manually specified
    # "default_icon_parents": "fas fa-folder",
    # "default_icon_children": "fas fa-folder",
    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": "css/main.css",
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,
    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    # "changeform_format": "vertical_tabs",
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
}

AZZMIN_UI_TWEAKS: dict = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-primary",
    "accent": "accent-navy",
    "navbar": "navbar-primary navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-light-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": True,
    "theme": "yeti",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-success",
    },
}
