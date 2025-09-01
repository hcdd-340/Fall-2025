---
title: HCDD 340 — Assignment 01
lang: en
date-meta: 2025-09-02
css: ../../tufte.css
toc: true
toc-depth: 3
toc-title: Table of Content
include-before: |
    <article>

include-after: |
    </article>
---


<section>
## Description
<label for="mn-ack" class="margin-toggle">&#8853;</label>
<input type="checkbox" id="mn-ack" class="margin-toggle"/>
<span class="marginnote">
    Inspired from the [MDN challenge](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Fundamental_CSS_comprehension)
</span>

This assignment will focus on displaying a Penn State profile. Please use the starter file in Canvas (Files → Assignment → Assignment-01). You will **only** update the CSS rules for the assignment (i.e., no need to change `index.html`)


The completed assignments should look something similar to:

![](./images/hcdd-340-assignment-01-screenshot-2025-08-31.png){ style="max-inline-size: 100%; max-width: 385px; block-size: auto; object-fit: cover;" }

</section>



<section>
## Deliverables
Please upload the following files (as a zip file):

* **Two screenshots** of the page in
	* Chrome
	* Firefox

* Your **code folder**. For grading, we will open the `index.html` in a browser. The uploaded folder must be self-contained — please make sure that there is no error when loading `index.html` in a browser

</section>

<section>
## Requirements & Rubrics

### Step 1 — Setup

* Create a new CSS file in the same directory as `index.html`

* Link the CSS file in `index.html` (hint: use `<link>` tag) (**1 pt**)

### Step 2 — First set of rules
We will use the provided `style-hints.txt` file to write the first set of CSS rules:

* Copy the common rules (the top 3 ones) to your CSS file (**1 pts**)

* Next you will have to match the following selectors with their declarations within `style-hints.txt` (**1 pts**)
	* `.card article img`
		* It should have `max-height` of 100% (so that it can grow or shrink depending on the parent container height)
	* `.card header`
		* Should have a darker background (e.g., `#009CDE`) and border radius of `1.4em` (for rounded corner — you can try different values) 
	* `.card footer`
		* Should have rounded corner
	* `.card`
		* Should have a black border with a border-radius of `1.5em` (for rounded corners). It should have a Penn State color as background (e.g., `#96BEE650`)

* There are two errors in the declarations, please fix those errors (**1 pts**)

	* Hint: Take a look at the Warnings and Errors in Firefox Dev Tools

### Step 3 — Adding new rules

* Write a rule that targets both header and footer (**2 pt**)

	* They should have 40% of the height (combined) of the card 

* Make sure that the `article` element has 60% of the height of the card (**2 pt**)

* `<p>` inside the `article` should have:
	* effective font-size of 19.2px, but expressed in `em` (**1 pt**)
	* it should have a padding of `1em` (**1 pt**)
	* all text should be center-aligned (**1 pt**)
	* the first line (i.e., profile name) should be 1) bold; and 2) with an effective font-size of 20.8px (but defined in `em`s) (**2 pts**)

* `<h2>` within the `header` element should have:
	* effective font size of 24.0px (but defined in `em`s) (**1 pt**)
	* a reasonable line height (e.g., 1.2? 1.5?) (**1 pt**)

* `<p>` within `footer` should have:
	* effective font size of 24.0px (but defined in `em`s) (**1 pt**)
	* should `float` right (so that all icons are sticking to the right side) (**1 pt**)

</section>

<section>
## Implementation suggestions

* To represent font-sizes using `em` values, you will have to figure out the base font size. You can check the Dev Tool to figure it out (also, we define it in the `style-hints.txt`)
* Given the elements are contained within the `.card`, you might consider using descendant relationships for different rules.
* You can use the Dev Tool to see different computed values

</section>
