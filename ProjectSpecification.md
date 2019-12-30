Full Stack Frameworks with Django Milestone ProjectProject purpose:

In this project, you'll build a full-stack site based around business logic used to control a centrally-owned dataset. You will set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.
Value provided:

By authenticating on the site and paying for some of its services, users can advance their own goals. Before authenticating, the site makes it clear how those goals would be furthered by the site.
The site owner is able to make money by providing this set of services to the users. There is no way for a regular user to bypass the site's mechanisms and derive all of the value available to paid users without paying.
Project RequirementsMain Technologies

    HTML, CSS, JavaScript, Python+Django

    Postgres

    Stripe payments

    Additional libraries and APIs
Mandatory Requirements

A project violating any of these requirements will FAIL
    Relational Database: Build a Django project backend by a relational database to create a website that allows users to store and manipulate data records about a particular domain.
    Multiple Apps: The project must be a brand new Django project, composed of multiple apps (an app for each potentially reusable component in your project).
    Design: Put some effort into designing a relational database schema well-suited for your domain. Make sure to put some thought into the relationships between entities. Create at least 2 custom django models beyond the examples shown on the course
    User Authentication: The project should include an authentication mechanism, allowing a user to register and log in, and there should be a good reason as to why the users would need to do so. e.g., a user would have to register to persist their shopping cart between sessions (otherwise it would be lost).
    User Interaction: Include at least one form with validation that will allow users to create and edit models in the backend (in addition to the authentication mechanism).
    Use of Stripe: At least one of your Django apps should contain some e-commerce functionality using Stripe. This may be a shopping cart checkout, subscription-based payments or single payments, donations, etc. After paying successfully, the user would then gain access to additional functionality/content on the site. Note that for this project you should use Stripe's test functionality, rather than actual live payments.
    Structure and Navigation: Incorporate a main navigation menu and structured layout (you might want to use Bootstrap to accomplish this).
    Use of JavaScript: The frontend should contain some JavaScript logic to enhance the user experience.
    Documentation: Write a README.md file for your project that explains what the project does and the value that it provides to its users.
    Version Control: Use Git & GitHub for version control.
    Attribution: Maintain clear separation between code written by you and code from external sources (e.g. libraries or tutorials). Attribute any code from external sources to its source via comments above the code and (for larger dependencies) in the README.
    Deployment: Deploy the final version of your code to a hosting platform such as Heroku.
    Make sure to not include any passwords or secret keys in the project repository. Make sure to turn off the Django DEBUG mode, which could expose secrets.

Project Example Idea 1

Build an issue tracker
External user’s goal:

    Report and track work on bugs and other issues with a product they like

Site owner's goal:

    Get user's feedback to guide prioritisation

    Get money to fund work on future features

Potential features to include:

    Now that you’re a full-fledged web developer you’ve decided it’s probably time for you to start your very own cool, modern startup, offering the extremely awesome UnicornAttractor web app to your users. It’s really really amazing, but we don’t care about it at all in this project. The exciting thing is the business model that you’ve decided upon – you chose to offer the service and bug fixes for free, but ask for money from your users to develop additional features.

    The primary entity in the Issue Tracker is a ticket describing a user’s issue, and similar to Github’s issue tracker, you should allow users to create tickets, comment on tickets, and show the status of the ticket (e.g. ‘to do,’ ‘doing,’ or ‘done’). As mentioned, issues come in two varieties – ‘bugs’ (which you’ll fix for free, eventually), and ‘features’ which you’d only develop if you’re offered enough money. To help you prioritize your work, your users will be able to upvote bugs (signifying ‘I have this too’), and upvote feature requests (signifying ‘I want to have this too’). While upvoting bugs is free, to upvote a feature request, users would need to pay some money (with a minimum amount of your choice) to pay for your time in working on it. In turn, you promise always to spend at least 50% of your time working on developing the highest-paid feature.

Advanced potential feature (nice-to-have)

    To offer transparency to your users, create a page that contains some graphs showing how many bugs or features are tended to on a daily, weekly and monthly basis, as well as the highest-voted bugs and features. To enhance the user experience, use dc.js (or any other js approach) to create dynamic charts.

    Add any additional pages that would help you attract users to the Issue Tracker (and have them pay you well). To make the users participate as much as possible in your online community, make sure that your UI/UX is sublime. Feel free to add additional features, such as a blog, extra perks for active participants, etc.

    If you want to have some more fun with this, feel free to add pages describing your fictional UnicornAttractor application.



Assessment Criteria

Your User Centric Front End Development project will be assessed based on the following criteria:
    Usability and Visual Impact:
        Project Purpose
        UX design
        Suitability for purpose
        Navigation
        Ease of use
        Information Architecture
        Defensive Design
    Layout and Visual Impact:
        Responsive Design
        Image Presentation
        Colour scheme and typography
    Code Quality:
        Appropriate use of HTML
        Appropriate use of CSS
        Appropriate use of JavaScript
        Appropriate use of Python
        Appropriate use of the template language
        Appropriate use of Django
    Application Features:
        App logic
        Cross-app logic
        E-commerce
        Authentication and Security
    Software Development practices:
        Directory Structure and File Naming
        Version control
        Testing implementation
        Testing write-up
        Readme file
        Comments
        Data store integration
        Deployment implementation
        Deployment write-up
Explanation of Assessment Marks

Once you submit your milestone project, it will be reviewed by an external assessor and graded based on a particular set of criteria, specific to each module. On each criterion, the assessor will review how your project meets this criterion and award you a mark between 0 to 5:

0 marks - Entirely missing
    The requirements for this criterion were completely ignored
1 mark - Non Functioning
    The criterion is only partially implemented and remains essentially non functioning
2 marks - Fails to Meet Expectations
    The criterion is mostly satisfied but has significant technical issues or other flaws
3 marks - Meets Expectations
    The criterion is fully satisfied without any significant issues, but is otherwise simple and doesn’t demonstrate any striving for excellence
4 marks - Exceeds Expectations
    The criterion is satisfied in a fully professional manner and demonstrating that the student strived for excellence, even if there are perhaps 1 or 2 minor issues.
5 marks - Greatly Exceeds Expectations
    The criterion was implemented flawlessly, exhibiting a well-planned approach and excellent execution; this project should be showcased for other students to learn from.

