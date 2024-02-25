# Escape Room Application

This application allows you to create and manage a digital escape room experience using Wagtail CMS. Participants navigate through various rooms by solving puzzles and finding keys that unlock new rooms, providing a flexible framework for creating engaging and interactive adventures.

## How the Escape Room Works

Participants start at the Homepage and navigate through the rooms by solving puzzles. Each room can grant them keys to unlock new rooms or reveal further content within the same room, depending on how you set up the keys and content. The structure is flexible, allowing you to create a customized experience.


## Getting Started

### Running the Application

1. **Build the Docker Image:** Ensure Docker is installed on your system. Navigate to the root directory of this project and build the Docker image using the provided Dockerfile.

   ```sh
   docker build -t escaperoom .
   ```

2. **Run the Container:** Start the application by running the Docker container.

   ```sh
   docker run -p 8000:8000 escaperoom
   ```

   The application should now be accessible at `http://localhost:8000`.

---

## Pre-configured Database

This application comes with a pre-configured `db.sqlite3` file to help you get started quickly. This includes a default admin user that you can use to log into the Wagtail CMS and Django admin interfaces immediately after starting the application.

### Login Details

- **Username:** admin
- **Password:** admin

### Accessing the Admin Interfaces

#### Wagtail CMS Admin

To log into the Wagtail CMS, navigate to:

```
http://127.0.0.1:8000/admin
```

Here, you can manage your escape room's pages, including the Homepage and RoomPages, as well as configure the main menu and user permissions.

#### Django Admin

The Django admin interface provides additional control over the application's models and settings. To access the Django admin, go to:

```
http://127.0.0.1:8000/django-admin
```

In the Django admin, you can manage users, groups, and low-level model details that are not exposed in the Wagtail CMS admin. Most likely you won't need to use the Django admin for typical escape room management tasks.

### First Steps After Login

Upon logging in for the first time, it's recommended to explore the Wagtail CMS interface to familiarize yourself with the structure of the escape room application. Consider updating the default admin password for security and reviewing the pre-configured pages to understand how they are set up.

---

## Setting Up an Escape Room with an empty database

### Configure settings.py

1. Open `escaperoom/settings.py` and set the `DATABASES` configuration to use a new database. The most simple is a local SQLite database, which is already configured in the settings file. You can change the `NAME` field to use a different file name if you wish.

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'new_db.sqlite3',
       }
   }
   ```

To use a different database, such as PostgreSQL or MySQL, update the `DATABASES` configuration accordingly. You can find more documention on how to configure the database in the [Django documentation](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASES).

2. Run the migrations to create the database schema.

   ```sh
   docker run -it -p 8000:8000 escaperoom python manage.py migrate
   ```

3. Create a superuser to access the Wagtail CMS and Django admin interfaces.

   ```sh
   docker run -it -p 8000:8000 escaperoom python manage.py createsuperuser
   ```

4. Start the application.

   ```sh
   docker run -p 8000:8000 escaperoom
   ```

5. Access the Wagtail CMS and Django admin interfaces to start creating your escape room.


--- 

## Creating an Escape Room in Wagtail CMS

### Creating a Homepage

First, create a Homepage for your escape room. This will serve as the entry point for participants.

1. Navigate to the Wagtail CMS admin interface at `http://127.0.0.1:8000/admin`.
2. Go to "Pages" and create a new page and select "Homepage" as the page type.
3. Fill in the details for the Homepage, including the title and body.
4. Publish the page.

IMPORTANT: You should setup the Homepage as the root page of the site. This can be done by going to the "Settings" -> "Sites" section of the Wagtail CMS admin and selecting the Homepage as the root page. This will ensure that the Homepage is the first page participants see when they access the escape room. When running locally the site is 127.0.0.1 and port is 8000. 

#### Homepage Fields

- **Title:** The name of your escape room, displayed prominently on the homepage.
- **Body:** A welcome message or introduction to the escape room experience.

### Adding Rooms

Add rooms as children of the Homepage. Each room can have its own puzzles, keys, and narrative.

1. From the Homepage, add a child page.
2. Select "RoomPage" as the page type and fill in the details.

#### RoomPage Fields

- **Title:** The name of the room.
- **Unlock Key:** The key required to access this room. Leave blank if no key is needed.
- **First Stage Body:** The initial content or puzzle of the room after the room is unlocked.
- **Second Stage Unlock Key:** The key to unlock the second stage within the room. 
- **Second Stage Body:** Additional content unlocked with a second key, for a layered puzzle experience. Most of the times you give a hint or a clue to the next room and the key to unlock it.

### Menu Configuration

For a page to appear in the navigation menu, it must be marked as visible in the menu. To add pages to the menu:
1. Make sure that a page is set to be visible in the menu. This can be done by checking the "Show in menus" checkbox in the "Promote" tab when editing a page. 
2. Navigate to Wagtail CMS -> Settings -> Main menu.
3. Add the visible pages and reorder them as needed.

### Submenus and Room Hierarchies

Creating rooms as children of another RoomPage allows you to create submenus in the navigation. The parent room acts as a container or grouping mechanism and does not serve as a puzzle room itself. This is useful for organizing your escape room into sections or themes.

---

## Additional Notes

- **Customization:** Feel free to customize the look and feel of the escape room by extending the templates and static files.
- **User Management:** Wagtail CMS provides robust user management features, allowing you to control access to the CMS for creating and updating rooms with multiple users!

Enjoy building your digital escape room experience!