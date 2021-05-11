# Recipe Cluster
Recipe Cluster is designed for gastronomy lovers. Save your favourite food and drink recipes.
Easily navigate through the application, adding, editing and deleting recipes as you wish.
Our forms are designed so you will be able to custom save your recipes and grab every last detail !
Search though other users recipes for inspiration. Our aim is to keep your recipes all in one place so you can foucus on cooking up a storm!

## UX/UI  
### Planes Of Scope

1. **Stratagy Plane**
* I Focused on what the user usually questioned when asking about a recipe and the main inforation included in the average recpie and that the application would cater for their needs and wants. 

2. **Scope Plane**
* I thought of the features and usuabilty of the applcation and how it would help the user in creating and storing their recipes.

3. **Structure Plane**
* At this stage of the porject after going through the features I wanted on the application, I started designing the structure of the applcation and what pages it would need.

4. **Skeleton Plane**
* After selecting the pages and designing the flow of the application, I started visualizing the layout, buttons, colors and fonts that would appeal to the user.

5. **Surface Plane**
* Bringing all the other stages together I started building the project and adjusting to changes and new implements on the way.

### User Stories

* **As A User Of Recipe Cluster**
1. I would like somewhere to store my recipes.
2. I would like the application to be easy to use.
3. I would like multiple fields to add different information about my recipe.
4. I would like to be able to search recipes.
5. I would like to be able to update and delete my recipes.

* **As A Developer Of Recipe Cluster**
1. Implementing the CRUD functionality.
2. Learning to use MONGDB.
3. Ensuring my application is user friendly.
4. Giving the user multiple parameter to add about each recipe.
5. Letting the user access their stored data easily.

### Features

1. **Navbar**

* The navbar is made up of 5 Links : Clickable Logo, All Recipes, My Recipes, Add Recipes, Resources.
When logged in "Log Out" is displayed in the navbar. When not logged in we have a "Sign up" and "Log In" links also
displayed in the navbvar. I chose green for the color of the navbar as it is the colour symolized with health and also most fresh produce "Eat your greens".

* I also added a mobile navabr for use on other divices.

2. **Images**

* I used images with alot of colour to entise the user. The images show different types of meals and alot of fresh ingredients.
I thought these images fitted my idea and what I was trying to bulid. They may also inspire the user to use fresher produce.

3. **Recipe Forms**

* One of the main features of the application is storing the recipes information. The form consits of numorous fields which the user can add different information about the recipe such as :
Cusine, Type, Ingredients and more. The from appears on both the "Add Recipe Page" and "Edit Recipe Page.

4. **Search Box**

* The search box allows user to search recipe by : Name, Cuisine and type of meal.

5. **Collapsible Recipe List**

* The collapsible recipe list shows user the recipes that have been added to the application along with another collapsible recipe list on the users profile page.
The list on the users page is just the recipes they have created themselves. The collapsible also has a delete and edit button, onll available to the user who created them.

6. **Resources Page**

* The recources page has links to various blogs, YouTube channels, books, equipment and ingredient sites I thought the user would enjoy or benefit from.

7. Sign Up, Login, Logout

* Other features of my application are been able to register as a user and log in and log out of your profile.

### Design & Visual

1. **Fonts & Color**

* I imported "Itim" from Google Fonts to use as my primary font and have "sans-serif" as my backup.
I liked the simplicitly in the sytling. It is also reasy to read.

* For my headers on the pages i picked green as the colour again to match with my Navbar.

* Paragraphs are in black color. I feel black is such a neautral colour and people are accustomed to seeing it.
Also its very easy to read.

* The background color of my pages is white. As it makes the features of the webpage stand out. Also it works well for readability with the black text
of my paragraphs.

2. **Icons**

* I Used icons while makes my recipe forms and also the sign up, login and logout pages. I used icons in which the field the user was using to was relative to what it was.

3. **Structure**

* The overall layout and structure is relatively simple. I focused on the user been able to user the application for its intended purpose. Straight to the point.
My pages with user content consist of a header follwed by an image. Below the image is a short sentance or paragraph explaing what the page does. Below then it the main feauture or purpose of the page.

### Wireframes

## Technologies Used

1. **Languages**

* I used HTML, CSS, JavaScript and jQuery as my front end languages.

* I used Python & Flask as my backend languages.

2. **Database**

* I used MONGDB as my database.

* I installed Pymongo to conect Flask & MONGODB.

3. **Layout & Styling**

* I used Googles Materialize to style and format some of my layouts and structures.

* I used FontAwesome for my icons.

4. **Depolyment**

* My Project is Depolyed both on GitHub & Heroku.

## Testing

### Validation Testing

* I validated my HTML through [W3C HTML Validator](https://validator.w3.org/#validate_by_input),
no errors except the ninja templating.

* I validated my CSS through [W3C CSS Validator](https://jigsaw.w3.org/css-validator/),
in which no errors were found either.

### Links

* I tested all links in the application to make sure they were not broken or faulty. 
All links bought me to where was designed.

### Forms

* Forms were tested multiple times with different inputs left out to check for required attribute.
Also dropdowns were vigoursly tested to ensure no faults with selection.

### Buttons

* Buttons were tested to ensure they compleated the action they were required to do.

## Bugs

**Here are some bugs I ran into along the way**

1. On making my drop down option, when saved and opened again for editing they would not save the choosen option.

* This is my code before:

      <option value="Breakfast">Breakfast</option>

* This is my code after:

      <option value="Breakfast" {%if recipe.recipe_type=="Breakfast"%} selected {% endif %}>Breakfast</option>

* I had to write a ninja statement for the dropdown option picked to be saved upon opening to edited where it then displayed.

2. I wanted to display the added recipes to both the main recipes page and the users page. The users page just the recipes they had created themselves.

* This is my code before:

      @app.route("/profile/<username>", methods=["GET", "POST"])
      def profile(username):
      # grab the session user's username from db
      username = mongo.db.users.find_one(
          {"username": session["user"]})["username"]

      if session["user"]:
          return render_template("profile.html", username=username)

      return redirect(url_for("login"))

* This is my code after:

      @app.route("/profile/<username>", methods=["GET", "POST"])
      def profile(username):
          recipes = list(mongo.db.recipes.find({'created_by': session['user']}))
          # grab the session user's username from db
          username = mongo.db.users.find_one(
              {"username": session["user"]})["username"]

      if session["user"]:
      return render_template("profile.html", username=username, recipes=recipes)

      return redirect(url_for("login"))

* I queried my profile view to look for my recipes in MONGODB to add them to my profile page.
  I added the recipe varible then to my

      if session["user"]:

3. After adding a recipe or editing a recipe. After submiting it I wanted to be redirected to the users profile page.

* This is my code before:

      return redirect(url_for("get_recipes"))

* This is my code after: 

    redirect(url_for("profile", username=session["user"]))

* The same logic was applied to both "Add Recipe" & "Edit Recipe".

4. My dropdown list for my allergens, when not picked was displaying the word "None" on the recipe page if not picked where it should be blank.

* This is my code before:

      <p><strong class="green-text">Allergens</strong> : {{ recipe.recipe_allergens }}</p>

* This is my code after:

      <p><strong class="green-text">Allergens</strong> : {% if recipe.recipe_allergens is not none %} {{ recipe.recipe_allergens }}{% endif %}</p>

* I applied a ninja if statement to check if nothing was picked to display nothing.


## Deployment

This project was developed using **Gitpod** , commited to **GitHub** using the build in terminal.

* To deploy the page to **GitHub** :

1. Log into **GitHub**.

2. From list of repositories on the left side, click **SmokeySam/my-recipe-cluster**.

3. Select **Settings** from the menu located at the top.

4. Scroll down to **GitHub Pages**.

5. Under **Source** click the menu labeled none and select **Master Branch**.

6. After selecting **Master Branch** the page is automatically refreshed, the website is now deployed.

7. Go back to the **GitHub Pages** section to retrieve the link to the deployed website.

* To clone this project from **GitHub**.

1. Go to the repository for this project. [my-recipe-cluster](https://github.com/SmokeySam/my-recipe-cluster).

2. Under the repository name click **"Clone or Download"**.

3. In the clone HTTPS section, copy the clone URL for the repository.

4. In your local IDE open **GitBash**.

5. Change the current working directory to the location where you want the cloned directory to be made.

6. Type git clone, then the URL you copied.

       git clone https://github.com/SmokeySam/just-cater.git

7. Press **Enter**. Your local clone will be created.

* To deply on **Heroku**

1. Log into **Heroku**.

2. Go to **Settings** at the top of the page.

3. Select **Reveal Config Vars**

4. Add your applications **Vars** 
Such as your : "IP" , "MONGO_DBNAME", "MONGO_URI", "PORT" and "SECRET_KEY".

5. Go back to **Settings** and click **Deploy**.

6. Connect your **GitHub** account.

7. Select **Manual Deploy** and select **Master Branch**

8. Heroku should now deploy your application.




## Credits

### Content

I used various resources to find the information I was seeking.

* I read posts on [Stack Over Flow](https://stackoverflow.com/), Google and Reddit.

* Watched YouTube videos explaing some of the **Technologies** ive listed previously.

* Followed a series of videos by **The Code Institute** on how to make a CRUD application.

* I used Google to find out information about the links on "Resouces Page"

### Media

* Images were taken off [Usplash](https://unsplash.com/).


    







