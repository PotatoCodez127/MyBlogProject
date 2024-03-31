<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!--
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/PotatoCodez127/MyBlogProject">
    <img src="Images/Python-Dark.svg" alt="Logo" width="90" height="90">
  </a>

<h3 align="center">My Flask Blog Project</h3>

  <p align="center">
    This is a project to show the usage of various libraries revolving mainly around Flask and Bootstrap.
    See <a href="#built-with">here</a> for all libraries and frameworks used in this project.
    <br />
    <a href="https://github.com/PotatoCodez127/MyBlogProject"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/PotatoCodez127/MyBlogProject">View Demo</a>
    ·
    <a href="https://github.com/PotatoCodez127/MyBlogProject/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/PotatoCodez127/MyBlogProject/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

This is a project to show the usage of various libraries revolving mainly around Flask and Bootstrap.     See <a href="#built-with"> _here_ </a> for all libraries and frameworks used in this project.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python]][Python-url]
* [![Flask]][Flask-url]
* [![SQLAlchemy]][SQLAlchemy-url]
* [![Jinja]][Jinja-url]
* [![werkzeug]][werkzeug-url]
* [![Bootstrap.com]][Bootstrap-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
This is an example of how you can setup your project locally.
To get a local copy up and running follow these simple example steps.

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/PotatoCodez127/MyBlogProject.git
   ```

2. Create a `.env` file for environment variables

3. Create a `Flask_SECRET_KEY` vairable for the secret key
   ```flask
   Flask_SECRET_KEY = 'RANDOM STRING FOR KEY';
   ```
4. Inside the `main.py` replace line `48` and `49`
   ```
   OWN_EMAIL = "YOUR OWN EMAIL ADDRESS"
   OWN_PASSWORD = "YOUR EMAIL ADDRESS PASSWORD"
   ```
   With your own email adress and set up an app password through google for your Flask app for the password field.
   
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Create basic Blog application with `Flask`.
- [x] Add `Bootstrap` into `HTML` templates and page routing.
- [x] Create an API endpoint to display blog data
- [x] Add `CRUD` operations
- [x] Add dynamic data to HTML templates using `Jinja`
- [x] Create a `SQLite` database and impliment `SQLAlchemy`
- [x] Create User authentication
- [x] Create forms with `Flask-wtf` to 'Sign up' and 'Log-in'
- [x] Add security to encrypt or hash passwords with `Werkzeug`
- [x] Add administrator roles so users cannot add/delete/ posts
- [x] Add a comment section to posts
- [ ] Deploy website

See the [open issues](https://github.com/PotatoCodez127/MyBlogProject/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

My email adress: jeandre.c127@gmail.com

Project Link: [https://github.com/PotatoCodez127/MyBlogProject](https://github.com/PotatoCodez127/MyBlogProject)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/PotatoCodez127/MyBlogProject.svg?style=for-the-badge
[contributors-url]: https://github.com/PotatoCodez127/MyBlogProject/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/PotatoCodez127/MyBlogProject.svg?style=for-the-badge
[forks-url]: https://github.com/PotatoCodez127/MyBlogProject/network/members
[stars-shield]: https://img.shields.io/github/stars/PotatoCodez127/MyBlogProject.svg?style=for-the-badge
[stars-url]: https://github.com/PotatoCodez127/MyBlogProject/stargazers
[issues-shield]: https://img.shields.io/github/issues/PotatoCodez127/MyBlogProject.svg?style=for-the-badge
[issues-url]: https://github.com/PotatoCodez127/MyBlogProject/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: www.linkedin.com/in/jeandre-coetzee-642a892b8
[product-screenshot]: Images/image.png
[Python]: https://img.shields.io/badge/python-dfdfdf?style=for-the-badge&logo=python&
[Python-url]: https://www.python.org/
[Flask]: https://img.shields.io/badge/Flask-313131?style=for-the-badge&logo=flask&
[Flask-url]: https://flask-login.readthedocs.io/en/latest/
[SQLAlchemy]: https://img.shields.io/badge/SQLAlchemy-506942?style=for-the-badge&logo=SQLAlchemy&
[SQLAlchemy-url]: https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/
[Jinja]: https://img.shields.io/badge/Jinja-990000?style=for-the-badge&logo=Jinja&
[Jinja-url]: https://jinja.palletsprojects.com/en/3.1.x/
[werkzeug]: https://img.shields.io/badge/Werkzeug-f1c232?style=for-the-badge&logo=werkzeug&
[werkzeug-url]: https://werkzeug.palletsprojects.com/en/3.0.x/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
