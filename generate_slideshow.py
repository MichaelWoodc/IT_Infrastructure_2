import os

# Define the base URL and subdirectory
base_url = "https://michaelwoodc.github.io/IT_Infrastructure_2/joomla_backup/"
subdirectory = "joomla_backup"

# Path to the subdirectory
path = os.path.join(os.getcwd(), subdirectory)

# Get list of files in the subdirectory
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

# Generate JavaScript code
js_code = """
<script>
(() => {
    // List of images with URLs
    const images_list = [
"""

for filename in files:
    file_url = f"{base_url}{filename}"
    js_code += f"""
    {{
        "url": "{file_url}",
        "alt": "",
        "name": "{filename}",
        "link": ""
    }},
"""

# Remove the trailing comma from the last item and close the array
js_code = js_code.rstrip(",\n") + """
    ];

    // Generated by https://www.html-code-generator.com/html/image-slideshow-generator
    let slider_id = document.querySelector("#hcg-slider-1");

    // Append all images
    let dots_div = "";
    let images_div = "";
    for (let i = 0; i < images_list.length; i++) {
        // if no link without href="" tag
        let href = (images_list[i].link == "" ? "":' href="'+images_list[i].link+'"');
        images_div += '<a'+href+' class="hcg-slides animated"'+(i === 0 ? ' style="display:flex"':'')+'>'+
                        '<span class="hcg-slide-number">'+(i+1)+'/'+images_list.length+'</span>'+
                        '<img src="'+images_list[i].url+'" alt="'+images_list[i].name+'">'+
                        '<span class="hcg-slide-text">'+images_list[i].name+'</span>'+
                     '</a>';
        dots_div += '<a href="#" class="hcg-slide-dot'+(i === 0 ? ' dot-active':'')+'" data-id="'+i+'"></a>';
    }
    slider_id.querySelector(".hcg-slider-body").innerHTML = images_div;
    slider_id.querySelector(".hcg-slide-dot-control").innerHTML = dots_div;

    let slide_index = 0;

    const images = slider_id.querySelectorAll(".hcg-slides");
    const dots = slider_id.querySelectorAll(".hcg-slide-dot");
    const prev_button = slider_id.querySelector("#hcg-slide-prev");
    const next_button = slider_id.querySelector("#hcg-slide-next");

    const showSlides = () => {
        if (slide_index > images.length-1) {
            slide_index = 0;
        }
        if (slide_index < 0) {
            slide_index = images.length-1;
        }
        for (let i = 0; i < images.length; i++) {
            images[i].style.display = "none";
            dots[i].classList.remove("dot-active");
            if (i == slide_index) {
                images[i].style.display = "flex";
                dots[i].classList.add("dot-active");
            }
        }
    }

    prev_button.addEventListener("click", event => {
        event.preventDefault();
        slide_index--;
        showSlides();
    }, false);

    next_button.addEventListener("click", event => {
        event.preventDefault();
        slide_index++;
        showSlides();
    }, false);

    const dot_click = event => {
        event.preventDefault();
        slide_index = event.target.dataset.id;
        showSlides();
    }

    for (let i = 0; i < dots.length; i++) {
        dots[i].addEventListener("click", dot_click, false);
    }
})();
</script>
"""

# Save the generated code to a file
with open("slider_code.js", "w") as f:
    f.write(js_code)

print("JavaScript code has been generated and saved to 'slider_code.js'.")
