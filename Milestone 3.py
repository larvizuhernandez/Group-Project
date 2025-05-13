import tkinter as tk #GUI toolkit for Pythin
from tkinter import messagebox #Pop-up alerts
from tkinter import ttk #themed widgets
import random #Generates randomness
import winsound  # Plays Windows system sound
import webbrowser #Opens links in a browser


class TriviaGame:
    def __init__(self, master):
        self.master = master
        master.title("Trivia Game with Difficulty Selection")
        master.geometry("600x450")

        # Game parameters
        self.score = 0
        self.timer_duration = 30  # Seconds per question
        self.remaining_time = self.timer_duration
        self.timer_id = None
        self.questions = []  # Will be filled after difficulty selection

        # Load categorized questions
        self.load_questions()

        # Difficulty selection
        self.select_difficulty()

    def load_questions(self):
        """Organize questions by difficulty."""
        self.questions_by_difficulty = {
            "Easy": [
                {"question": "What household appliance keeps food cold?",
                 "options": ["Oven", "Refrigerator", "Microwave", "Dishwasher"],
                 "answer": "Refrigerator",
                 "url": "https://applianceupdate.com/what-does-the-refrigerator-do/"},
                {"question": "What do you use to measure temperature?",
                 "options": ["Spoon", "Thermometer", "Fork", "Knife"],
                 "answer": "Thermometer",
                 "url": "https://health.clevelandclinic.org/thermometers-how-to-take-your-temperature"},
                {"question": "What is the name of the famous ship that sank in 1912?",
                 "options": ["Titanic", "Lusitania", "Queen Mary", "Mayflower"],
                 "answer": "Titanic",
                 "url": "https://www.britannica.com/topic/Titanic"},
                {"question": "What is the name of the planet closest to the sun?",
                 "options": ["Venus", "Earth", "Mars", "Mercury"],
                 "answer": "Mercury",
                 "url": "https://science.nasa.gov/mercury/"},
                {"question": "What is the primary color of a ripe banana?",
                 "options": ["Green", "Red", "Yellow", "Blue"],
                 "answer": "Yellow",
                 "url": "https://stellinamarfa.com/fruits/what-is-the-colour-of-ripe-banana/"},
                {"question": "What is the largest mammal in the world?",
                 "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
                 "answer": "Blue Whale",
                 "url": "https://enviroliteracy.org/animals/what-is-the-largest-mammal-in-the-world/"},
                {"question": "What is the name of the space agency that landed the first human on the Moon?",
                 "options": ["ESA", "NASA", "Roscosmos", "CNSA"],
                 "answer": "NASA",
                 "url": "https://www.nasa.gov/specials/60counting/spaceflight.html"},
                {"question": "Who was the second President of the United States?",
                 "options": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "John Adams"],
                 "answer": "John Adams",
                 "url": "https://en.wikipedia.org/wiki/John_Adams"},
                {"question": "What is the capital of Mexico?",
                 "options": ["Guadalajara", "Monterrey", "Mexico City", "Tijuana"],
                 "answer": "Mexico City",
                 "url": "https://www.mappr.co/capital-cities/mexico/"},
                {"question": "What is the name of the animated movie about a clownfish searching for his son?",
                 "options": ["Finding Nemo", "The Little Mermaid", "Shark Tale", "A Bug’s Life"],
                 "answer": "Finding Nemo",
                 "url": "https://www.imdb.com/title/tt0266543/"},
                {"question": "What is the name of the famous theme park located in Orlando, Florida?",
                 "options": ["Disneyland", "Universal Studios", "Six Flags", "Walt Disney World"],
                 "answer": "Walt Disney World",
                 "url": "https://inqira.io/q/what-is-the-name-of-the-famous-theme-park-in-orlando-florida"},
                {"question": "What is the longest bone in the human body?",
                 "options": ["Tibia", "Femur", "Humerus", "Radius"],
                 "answer": "Femur",
                 "url": "https://my.clevelandclinic.org/health/body/22503-femur"},
                {"question": "What is the main language spoken in Brazil?",
                 "options": ["Spanish", "Portuguese", "French", "English"],
                 "answer": "Portuguese",
                 "url": "https://www.worldatlas.com/articles/what-languages-are-spoken-in-brazil.html"},
                {"question": "What is the smallest country in the world?",
                 "options": ["Monaco", "Vatican City", "San Marino", "Liechtenstein"],
                 "answer": "Vatican City",
                 "url": "https://www.britannica.com/topic/list-of-the-smallest-countries-by-area"},
                {"question": "Who invented the telephone?",
                 "options": ["Thomas Edison", "Alexander Graham Bell", "Nikola Tesla", "Albert Einstein"],
                 "answer": "Alexander Graham Bell",
                 "url": "https://www.britannica.com/biography/Alexander-Graham-Bell"},
                {"question": "What is the largest ocean on Earth?",
                 "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                 "answer": "Pacific Ocean",
                 "url": "https://www.usatoday.com/story/news/2022/12/13/what-is-largest-ocean-on-earth/8191191001/"},
                {"question": "What is the main ingredient in guacamole?",
                 "options": ["Tomato", "Avocado", "Onion", "Pepper"],
                 "answer": "Avocado",
                 "url": "https://spicerally.com/guacamole-and-its-ingredients/"},
                {"question": "What is the largest continent on Earth?",
                 "options": ["Africa", "Asia", "Europe", "Antarctica"],
                 "answer": "Asia",
                 "url": "https://www.worldatlas.com/articles/what-is-the-largest-continent.html"},
                {"question": "What is the main ingredient in traditional hummus?",
                 "options": ["Chickpeas", "Lentils", "Beans", "Peas"],
                 "answer": "Chickpeas",
                 "url": "https://thecookingfacts.com/what-is-a-primary-ingredient-for-hummus/"},
                {"question": "What is the capital of Canada?",
                 "options": ["Toronto", "Vancouver", "Ottawa", "Montreal"],
                 "answer": "Ottawa",
                 "url": "https://www.britannica.com/place/Ottawa"},
                {"question": "What is the main ingredient in a traditional Margherita pizza?",
                 "options": ["Pepperoni", "Mushrooms", "Tomatoes", "Pineapple"],
                 "answer": "Tomatoes",
                 "url": "https://gourmetglean.com/what-are-the-ingredients-of-a-margherita-pizza-and-why/"},
                {"question": "What is the capital of Spain?",
                 "options": ["Barcelona", "Seville", "Madrid", "Valencia"],
                 "answer": "Madrid",
                 "url": "https://www.britannica.com/place/Madrid"},
                {"question": "What is the capital of South Korea?",
                 "options": ["Busan", "Icheon", "Seoul", "Daegu"],
                 "answer": "Seoul",
                 "url": "https://www.britannica.com/place/Seoul"},
                {"question": "What is the capital of Argentina?",
                 "options": ["Buenos Aires", "Santiago", "Lima", "Montevideo"],
                 "answer": "Buenos Aires",
                 "url": "https://www.britannica.com/place/Buenos-Aires"},
                {"question": "In which sport do players aim to score goals by hitting a ball with a curved stick?",
                 "options": ["Lacrosse", "Field Hockey", "Polo", "Cricket"],
                 "answer": "Field Hockey",
                 "url": "https://icehockeycentral.com/what-is-field-hockey-the-beginners-guide/"}
            ],
            "Medium":
                [{"question": "Who wrote the Iliad?",
                  "options": ["Aristotle", "Homer", "Socrates", "Pythagorus"],
                  "answer": "Homer",
                  "url": "https://www.litcharts.com/lit/the-iliad/summary"},
                 {"question": "What does the “E” in PEMDAS stand for?",
                  "options": ["Equation", "Equal", "Even", "Exponent"],
                  "answer": "Exponent",
                  "url": "https://www.mathsisfun.com/operation-order-pemdas.html"},
                 {"question": "What is the second planet in the solar system?",
                  "options": ["Venus", "Mars", "Mercury", "Jupiter"],
                  "answer": "Venus",
                  "url": "https://science.nasa.gov/venus/"},
                 {"question": "Who is known as the King of Pop?",
                  "options": ["Elvis Presley", "Michael Jackson", "Prince", "Justin Bieber"],
                  "answer": "Michael Jackson",
                  "url": "https://www.britannica.com/biography/Michael-Jackson"},
                 {"question": "What year will the next leap year occur?",
                  "options": ["2026", "2030", "2028", "2027"],
                  "answer": "2028",
                  "url": "https://www.timeanddate.com/date/leapyear.html#:~:text=Leap%20years%20are%20years%20where,occur%20almost%20every%20four%20years."},
                 {"question": "When did Columbus Sail the Ocean Blue?",
                  "options": ["1942", "1834", "1773", "1492"],
                  "answer": "1492",
                  "url": "https://poemanalysis.com/in-1492-columbus-sailed-the-ocean-blue/"},
                 {"question": "What animal is the famous mascot of Disney?",
                  "options": ["A Dog", "A Cat", "A Mouse", "A Snake"],
                  "answer": "A Mouse",
                  "url": "https://mickey.disney.com/"},
                 {"question": "Words that describe actions are called what?",
                  "options": ["Verbs", "Nouns", "Adjectives", "Punctuation"],
                  "answer": "Verbs",
                  "url": "https://www.grammarly.com/blog/parts-of-speech/verbs/"},
                 {"question": "Solid, Liquid, and Gas are States of What?",
                  "options": ["Phases", "Matter", "Being", "Water"],
                  "answer": "Matter",
                  "url": "https://www.chem.purdue.edu/gchelp/atoms/states.html"},
                 {"question": "Steve Jobs co-founded which company?",
                  "options": ["Microsoft", "HP", "Apple", "Google"],
                  "answer": "Apple",
                  "url": "https://www.apple.com/stevejobs/"},
                 {"question": "Shakespeare’s Romeo and Juliet is about what kind of lovers?",
                  "options": ["Destined", "Fearful", "Genuine", "Star-crossed"],
                  "answer": "Star-crossed",
                  "url": "https://nosweatshakespeare.com/quotes/famous/star-crossed-lovers/"},
                 {"question": "Which of these animals is a mammal?",
                  "options": ["Snake", "Spider", "Bear", "Eagle"],
                  "answer": "Bear",
                  "url": "https://www.britannica.com/animal/bear"},
                 {"question": "What type of sand can you sink into when you move?",
                  "options": ["Quick", "Flat", "Wet", "Hot"],
                  "answer": "Quick",
                  "url": "https://en.wikipedia.org/wiki/Quicksand"},
                 {"question": "Which Continent is also a Country?",
                  "options": ["Antarctica", "Europe", "Australia", "Africa"],
                  "answer": "Australia",
                  "url": "https://kids.nationalgeographic.com/geography/countries/article/australia#:~:text=use%20is%20prohibited.-,Australia%20is%20the%20only%20country%20in%20the%20world%20that%20covers,third%20of%20Australia%20is%20desert."},
                 {"question": "What is your star sign called?",
                  "options": ["Zodiac", "Season", "Asteroid", "Star"],
                  "answer": "Zodiac",
                  "url": "https://www.zodiacsign.com/"},
                 {"question": "What kind of story specifically uses animals to teach a lesson?",
                  "options": ["Nonfiction", "Fiction", "Fable", "Nursery"],
                  "answer": "Fable",
                  "url": "https://en.wikipedia.org/wiki/Fable"},
                 {"question": "Which of these is NOT a season?",
                  "options": ["May", "Winter", "Fall", "Summer"],
                  "answer": "May",
                  "url": "https://www.timeanddate.com/calendar/aboutseasons.html"},
                 {"question": "How many Championship rings does Lebron James have?",
                  "options": ["5 rings", "6 rings", "4 rings", "3 rings"],
                  "answer": "4 rings",
                  "url": "https://www.sportskeeda.com/basketball/lebron-james-rings"},
                 {"question": "In the Bible, who slayed the Giant Goliath?",
                  "options": ["Daniel", "John", "Solomon", "David"],
                  "answer": "David",
                  "url": "https://www.britannica.com/biography/David"},
                 {"question": "In the Wizard of Oz, what type of animal was Cowardly?",
                  "options": ["Dog", "Lion", "Monkey", "Tiger"],
                  "answer": "Lion",
                  "url": "https://oz.fandom.com/wiki/Cowardly_Lion"},
                 {"question": "What animal is the official mascot of CSUMB?",
                  "options": ["Sea Lion", "Whale", "Sea Otter", "Dolphin"],
                  "answer": "Sea Otter",
                  "url": "https://csumb.edu/"},
                 {"question": "Hickory, Dickory, Dock, the mouse ran up the what?",
                  "options": ["Wall", "Sprout", "Vine", "Clock"],
                  "answer": "Clock",
                  "url": "https://americanenglish.state.gov/files/ae/resource_files/4-hickory-lyrics_0.pdf"},
                 {"question": "Carbs, Proteins, and Fats are known as what?",
                  "options": ["Vitamins", "MacroNutrients", "Energy", "Food"],
                  "answer": "MacroNutrients",
                  "url": "https://www.mdanderson.org/cancerwise/macronutrients-101--what-to-know-about-protein--carbs-and-fats.h00-159774078.html"},
                 {"question": "What kind of Planet is Pluto?",
                  "options": ["Dwarf", "Small", "Large", "It’s not a Planet"],
                  "answer": "Dwarf",
                  "url": "https://science.nasa.gov/dwarf-planets/pluto/"},
                 {"question": "Bill Nye is known as what kind of guy?",
                  "options": ["The Meteor Guy", "The Solar System Guy", "The History Guy", "The Science Guy"],
                  "answer": "The Science Guy",
                  "url": "https://www.billnye.com/"},
                 ],

            "Hard": [
                {"question": "What is the name of the famous ship that sank in 1912?",
                 "options": ["Titanic", "Lusitania", "Queen Mary", "Mayflower"],
                 "answer": "Titanic",
                 "url": "https://www.history.com/topics/early-20th-century-us/titanic"
                 },
                {
                    "question": "What is the longest river in the world?",
                    "options": ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"],
                    "answer": "Nile River",
                    "url": "https://www.britannica.com/place/Nile-River"
                },
                {
                    "question": "Who developed the theory of evolution by natural selection?",
                    "options": ["Charles Darwin", "Gregor Mendel", "Isaac Newton", "Albert Einstein"],
                    "answer": "Charles Darwin",
                    "url": "https://www.britannica.com/biography/Charles-Darwin"
                },
                {
                    "question": "Which element is known as the 'King of Chemicals'?",
                    "options": ["Sulfuric Acid", "Hydrochloric Acid", "Nitric Acid", "Acetic Acid"],
                    "answer": "Sulfuric Acid",
                    "url": "https://www.britannica.com/science/sulfuric-acid"
                },
                {
                    "question": "What is the capital city of Australia?",
                    "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
                    "answer": "Canberra",
                    "url": "https://www.britannica.com/place/Canberra"
                },
                {
                    "question": "Who was the first woman to win a Nobel Prize?",
                    "options": ["Marie Curie", "Rosalind Franklin", "Ada Lovelace", "Jane Goodall"],
                    "answer": "Marie Curie",
                    "url": "https://www.nobelprize.org/prizes/physics/1903/marie-curie/biographical/"
                },
                {
                    "question": "What is the hardest natural substance on Earth?",
                    "options": ["Diamond", "Graphite", "Corundum", "Quartz"],
                    "answer": "Diamond",
                    "url": "https://www.britannica.com/science/diamond-gemstone"
                },
                {
                    "question": "Which Shakespeare play features the characters Rosencrantz and Guildenstern?",
                    "options": ["Hamlet", "Macbeth", "Othello", "King Lear"],
                    "answer": "Hamlet",
                    "url": "https://www.britannica.com/topic/Hamlet-by-Shakespeare"
                },
                {
                    "question": "What is the chemical symbol for the element with the atomic number 1?",
                    "options": ["H", "He", "Li", "Be"],
                    "answer": "H (Hydrogen)",
                    "url": "https://www.britannica.com/science/hydrogen"
                },
                {
                    "question": "Who was the first President of the United States?",
                    "options": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"],
                    "answer": "George Washington",
                    "url": "https://www.whitehouse.gov/about-the-white-house/presidents/george-washington/"
                },
                {
                    "question": "What is the largest desert in the world?",
                    "options": ["Sahara Desert", "Gobi Desert", "Kalahari Desert", "Arabian Desert"],
                    "answer": "Sahara Desert",
                    "url": "https://www.britannica.com/place/Sahara-desert-Africa"
                },
                {
                    "question": "Which planet is known as the Red Planet?",
                    "options": ["Mars", "Venus", "Jupiter", "Saturn"],
                    "answer": "Mars",
                    "url": "https://www.britannica.com/place/Mars-planet"
                },
                {
                    "question": "Who wrote the play 'A Streetcar Named Desire'?",
                    "options": ["Tennessee Williams", "Arthur Miller", "Eugene O'Neill", "Edward Albee"],
                    "answer": "Tennessee Williams",
                    "url": "https://www.britannica.com/topic/A-Streetcar-Named-Desire-play-by-Williams"
                },
                {
                    "question": "What is the main ingredient in traditional Japanese miso soup?",
                    "options": ["Miso paste", "Soy sauce", "Tofu", "Seaweed"],
                    "answer": "Miso paste",
                    "url": "https://www.britannica.com/topic/miso"
                },
                {
                    "question": "Who discovered penicillin?",
                    "options": ["Alexander Fleming", "Louis Pasteur", "Robert Koch", "Joseph Lister"],
                    "answer": "Alexander Fleming",
                    "url": "https://www.britannica.com/biography/Alexander-Fleming"
                },
                {
                    "question": "What is the most abundant gas in the Earth's atmosphere?",
                    "options": ["Nitrogen", "Oxygen", "Carbon Dioxide", "Argon"],
                    "answer": "Nitrogen",
                    "url": "https://www.britannica.com/science/nitrogen"
                },
                {
                    "question": "Which artist painted the ceiling of the Sistine Chapel?",
                    "options": ["Michelangelo", "Leonardo da Vinci", "Raphael", "Donatello"],
                    "answer": "Michelangelo",
                    "url": "https://www.britannica.com/topic/Sistine-Chapel-ceiling"
                },
                {
                    "question": "What is the largest organ in the human body?",
                    "options": ["Skin", "Liver", "Heart", "Lungs"],
                    "answer": "Skin",
                    "url": "https://www.britannica.com/science/skin"
                },
                {
                    "question": "Who is the author of the Harry Potter series?",
                    "options": ["J.K. Rowling", "Stephen King", "J.R.R. Tolkien", "George R.R. Martin"],
                    "answer": "J.K. Rowling",
                    "url": "https://www.britannica.com/biography/J-K-Rowling"
                },
                {
                    "question": "What is the smallest unit of life?",
                    "options": ["Cell", "Atom", "Molecule", "Organ"],
                    "answer": "Cell",
                    "url": "https://www.britannica.com/science/cell-biology"
                },
                {
                    "question": "Which country is known as the Land of the Rising Sun?",
                    "options": ["Japan", "China", "South Korea", "Thailand"],
                    "answer": "Japan",
                    "url": "https://www.britannica.com/place/Japan"
                },
                {
                    "question": "Who was the first person to walk on the moon?",
                    "options": ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "Michael Collins"],
                    "answer": "Neil Armstrong",
                    "url": "https://www.nasa.gov/mission_pages/apollo/apollo11.html"
                },
                {
                    "question": "What is the chemical formula for water?",
                    "options": ["H2O", "CO2", "O2", "N2"],
                    "answer": "H2O",
                    "url": "https://www.britannica.com/science/water"
                },
                {
                    "question": "Which ancient civilization built the pyramids?",
                    "options": ["Egyptians", "Mayans", "Aztecs", "Romans"],
                    "answer": "Egyptians",
                    "url": "https://www.britannica.com/topic/pyramid-architecture"
                },
                {
                    "question": "What is the capital city of Canada?",
                    "options": ["Ottawa", "Toronto", "Vancouver", "Montreal"],
                    "answer": "Ottawa",
                    "url": "https://www.britannica.com/place/Ottawa"
                },
                {
                    "question": "Who wrote the novel 'Pride and Prejudice'?",
                    "options": ["Jane Austen", "Charlotte Brontë", "Emily Brontë", "Louisa May Alcott"],
                    "answer": "Jane Austen",
                    "url": "https://www.britannica.com/biography/Jane-Austen"
                }
            ],

            "Extremely Hard": [
                {"question": "Who was the last ruler of the Habsburg dynasty of Austria?",
                 "options": ["Franz Ferdinand", "Otto von Habsburg", "Maximilian I", "Charles I of Austria"],
                 "answer": "Charles I of Austria",
                 "url": "https://shunculture.com/article/did-austria-have-a-royal-family"},
                {"question": "What is the rarest naturally occurring element on Earth?",
                 "options": ["Francium", "Promethium", "Astatine", "Technetium"],
                 "answer": "Astatine",
                 "url": "https://enviroliteracy.org/what-is-the-rarest-naturally-occurring-element-on-earth/"},
                {"question": "Which novel by Herman Melville features the character Captain Ahab?",
                 "options": ["Billy Budd", "Moby-Dick", "Typee", "White-Jacket"],
                 "answer": "Moby-Dick",
                 "url": "https://www.sparknotes.com/lit/mobydick/"},
                {"question": "Who painted the famous work titled The Persistence of Memory?",
                 "options": ["Pablo Picasso", "Salvador Dalí", "Claude Monet", "Henri Matisse"],
                 "answer": "Salvador Dalí",
                 "url": "https://artincontext.org/the-persistence-of-memory/"},
                {"question": "Which composer is known for creating the famous The Four Seasons concertos?",
                 "options": ["Bach", "Mozart", "Beethoven", "Antonio Vivaldi"],
                 "answer": "Antonio Vivaldi",
                 "url": "https://en.wikipedia.org/wiki/The_Four_Seasons_(Vivaldi)"},
                {"question": "What was the name of the first artificial satellite to orbit Earth, launched in 1957?",
                 "options": ["Explorer 1", "Sputnik 1", "Luna 2", "Vanguard 1"],
                 "answer": "Sputnik 1",
                 "url": "https://www.britannica.com/technology/Sputnik"},
                {"question": "Who is the only player in NBA history to score 100 points in a single game?",
                 "options": ["Kobe Bryant", "Wilt Chamberlain", "Michael Jordan", "LeBron James"],
                 "answer": "Wilt Chamberlain",
                 "url": "https://www.espn.com/nba/story/_/id/39367091"},
                {"question": "Which planet in our solar system has the most moons?",
                 "options": ["Saturn", "Neptune", "Uranus", "Jupiter"],
                 "answer": "Jupiter",
                 "url": "https://www.usatoday.com/story/news/2022/08/12/which-planet-has-most-moons-solar-system/10246652002/"},
                {"question": "Who won the Academy Award for Best Director for the movie The Shape of Water?",
                 "options": ["Guillermo del Toro", "Alfonso Cuarón", "Steven Spielberg", "James Cameron"],
                 "answer": "Guillermo del Toro",
                 "url": "https://www.nbcnews.com/pop-culture/awards/shape-water-wins-best-picture-90th-academy-awards-n853531"},
                {"question": "In Greek mythology, who was the king of the gods and ruler of Mount Olympus?",
                 "options": ["Hades", "Poseidon", "Apollo", "Zeus"],
                 "answer": "Zeus",
                 "url": "https://www.greekmyths-greekmythology.com/zeus-king-of-the-gods/"},
                {"question": "Who is known for writing the philosophical treatise The Republic?",
                 "options": ["Plato", "Aristotle", "Socrates", "Descartes"],
                 "answer": "Plato",
                 "url": "https://en.wikipedia.org/wiki/Republic_(Plato)"},
                {
                    "question": "What was the name of the economic theory proposed by John Maynard Keynes during the Great Depression?",
                    "options": ["Supply-Side Economics", "Monetarism", "Keynesian Economics", "Classical Economics"],
                    "answer": "Keynesian Economics",
                    "url": "https://www.investopedia.com/terms/k/keynesianeconomics.asp"},
                {"question": "Which mammal is known to have the longest gestation period?",
                 "options": ["Blue Whale", "Giraffe", "African Elephant", "Rhino"],
                 "answer": "African Elephant",
                 "url": "https://www.treehugger.com/animals-with-the-longest-gestation-period-4869368"},
                {"question": "What is the main ingredient in the Japanese dish temaki?",
                 "options": ["Seaweed", "Tofu", "Nori", "Salmon"],
                 "answer": "Nori",
                 "url": "https://www.foodrepublic.com/1292625/what-is-temaki-is-it-the-next-big-trend/"},
                {
                    "question": "Who is considered the father of modern surgery and invented the surgical procedure of antiseptic surgery?",
                    "options": ["Edward Jenner", "Joseph Lister", "Alexander Fleming", "Louis Pasteur"],
                    "answer": "Joseph Lister",
                    "url": "https://healthdor.com/article/joseph-lister-the-father-of-modern-antiseptic-surgery"},
                {"question": "Which language is considered the official language of Vatican City?",
                 "options": ["Italian", "Latin", "French", "German"],
                 "answer": "Latin",
                 "url": "https://www.babbel.com/en/magazine/vatican-language"},
                {"question": "What is the name of the world’s tallest building, located in Dubai?",
                 "options": ["Burj Khalifa", "Shanghai Tower", "Abraj Al-Bait", "One World Trade Center"],
                 "answer": "Burj Khalifa",
                 "url": "https://thetowerinfo.com/buildings-list/burj-khalifa/"},
                {"question": "Who proposed the theory of general relativity?",
                 "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
                 "answer": "Albert Einstein",
                 "url": "https://www.britannica.com/science/general-relativity"},
                {
                    "question": "In the TV show Breaking Bad, what is the real name of the character known as 'Heisenberg'?",
                    "options": ["Jesse Pinkman", "Walter White", "Saul Goodman", "Hank Schrader"],
                    "answer": "Walter White",
                    "url": "https://screenrant.com/breaking-bad-walter-white-heisenberg-name-alias-meaning/"},
                {"question": "What element has the atomic number 79?",
                 "options": ["Gold", "Silver", "Platinum", "Copper"],
                 "answer": "Gold",
                 "url": "https://www.periodic-table.org/gold-atomic-number/"},
                {"question": "What is the name of the largest known prime number (as of 2021)?",
                 "options": ["Fermat Prime", "Euler Prime", "Mersenne prime (2^82,589,933 − 1)", "Twin Prime"],
                 "answer": "Mersenne prime (2^82,589,933 − 1)",
                 "url": "https://math.answers.com/basic-math/What_is_the_longest_known_prime_number"},
                {"question": "Who is credited with inventing the first practical telephone?",
                 "options": ["Graham Bell", "Nikola Tesla", "Edison", "Marconi"],
                 "answer": "Graham Bell",
                 "url": "https://www.loc.gov/everyday-mysteries/technology/item/who-is-credited-with-inventing-the-telephone/"},
                {"question": "Who wrote the classic novel 1984, which features the character Winston Smith?",
                 "options": ["George Orwell", "Aldous Huxley", "Ray Bradbury", "J.D. Salinger"],
                 "answer": "George Orwell",
                 "url": "https://www.sparknotes.com/lit/1984/character/winston-smith/"},
                {"question": "Which ancient wonder of the world was located in the city of Alexandria, Egypt?",
                 "options": ["The Great Pyramid", "Hanging Gardens", "The Lighthouse of Alexandria",
                             "Colossus of Rhodes"],
                 "answer": "The Lighthouse of Alexandria",
                 "url": "https://www.britannica.com/topic/lighthouse-of-Alexandria"},
                {"question": "Which professional soccer team is located in Barcelona, Spain?",
                 "options": ["Real Madrid", "Bayern Munich", "Borussia Dortmund", "Fc Barcelona"],
                 "answer": "Fc Barcelona",
                 "url": "https://www.britannica.com/topic/FC-Barcelona"}
            ]

        }

    def select_difficulty(self):
        """Prompt the user to select a difficulty level."""
        self.difficulty = tk.StringVar()
        difficulty_frame = tk.Frame(self.master)
        difficulty_frame.pack(pady=10)

        tk.Label(difficulty_frame, text="Select Difficulty:", font=("Helvetica", 14)).pack()

        for level in self.questions_by_difficulty.keys():
            tk.Radiobutton(difficulty_frame, text=level, variable=self.difficulty, value=level).pack()

        tk.Button(difficulty_frame, text="Start Game", command=lambda: self.start_game(difficulty_frame)).pack()

    def start_game(self, frame):
        """Start the game with the selected difficulty."""
        frame.destroy()
        self.questions = self.questions_by_difficulty[self.difficulty.get()]
        random.shuffle(self.questions)

        # Score label
        self.score_label = tk.Label(self.master, text=f"Score: {self.score}", font=("Helvetica", 14))
        self.score_label.pack(pady=10)

        # Timer label
        self.timer_label = tk.Label(self.master, text=f"Time left: {self.remaining_time} sec", font=("Helvetica", 14))
        self.timer_label.pack(pady=5)

        # Visual timer using a progress bar
        self.timer_progress = ttk.Progressbar(self.master, orient="horizontal", length=400, mode="determinate")
        self.timer_progress["maximum"] = self.timer_duration
        self.timer_progress["value"] = self.timer_duration
        self.timer_progress.pack(pady=5)

        # Question label
        self.question_label = tk.Label(self.master, text="Question will appear here", wraplength=550,
                                       font=("Helvetica", 12))
        self.question_label.pack(pady=20)

        # URL label
        self.url_label = tk.Label(self.master, text="", fg="blue", cursor="hand2", font=("Helvetica", 10, "underline"))
        self.url_label.pack(pady=5)

        # Answer buttons
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(pady=10)
        self.answer_buttons = []
        for i in range(4):
            btn = tk.Button(self.button_frame, text=f"Option {i + 1}", width=50,
                            command=lambda idx=i: self.check_answer(idx))
            btn.pack(pady=5)
            self.answer_buttons.append(btn)

        self.next_question()

    def next_question(self):
        """Load the next question and update the GUI."""
        if not self.questions:
            messagebox.showinfo("Game Over", f"All questions answered!\nFinal Score: {self.score}")
            self.master.destroy()
            return

        # Reset timer
        if self.timer_id:
            self.master.after_cancel(self.timer_id)
        self.remaining_time = self.timer_duration
        self.timer_label.config(text=f"Time left: {self.remaining_time} sec")
        self.timer_progress["value"] = self.timer_duration

        # Get a new question
        self.current_question = self.questions.pop()
        self.question_label.config(text=self.current_question["question"])

        # Update answer buttons text
        for idx, btn in enumerate(self.answer_buttons):
            btn.config(text=self.current_question["options"][idx], state=tk.NORMAL)

        # Update URL label
        self.url_label.config(text="Learn more here", fg="blue", cursor="hand2")
        self.url_label.bind("<Button-1>", lambda event: self.open_url(self.current_question["url"]))

        # Start the countdown timer
        self.countdown()

    def countdown(self):
        """Decrements the timer every second."""
        if self.remaining_time > 0:
            self.timer_label.config(text=f"Time left: {self.remaining_time} sec")
            self.timer_progress["value"] = self.remaining_time

            if self.remaining_time <= 5:
                winsound.Beep(1000, 200)

            self.remaining_time -= 1
            self.timer_id = self.master.after(1000, self.countdown)
        else:
            self.timer_label.config(text="Time left: 0 sec")
            self.timer_progress["value"] = 0
            messagebox.showinfo("Time's Up!", "Time's up! Moving to the next question.")
            self.disable_buttons()
            self.master.after(1000, self.next_question)

    def disable_buttons(self):
        """Disable answer buttons."""
        for btn in self.answer_buttons:
            btn.config(state=tk.DISABLED)

    def check_answer(self, idx):
        """Checks the user's answer."""
        if self.timer_id:
            self.master.after_cancel(self.timer_id)
        chosen_answer = self.current_question["options"][idx]
        if chosen_answer == self.current_question["answer"]:
            messagebox.showinfo("Correct!", "That is the correct answer!")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        else:
            messagebox.showinfo("Incorrect", f"Incorrect! The correct answer was: {self.current_question['answer']}")
        self.disable_buttons()
        self.master.after(1000, self.next_question)

    def open_url(self, url):
        """Open the link for additional learning."""
        webbrowser.open(url)


if __name__ == "__main__":
    root = tk.Tk()
    game = TriviaGame(root)
    root.mainloop()

