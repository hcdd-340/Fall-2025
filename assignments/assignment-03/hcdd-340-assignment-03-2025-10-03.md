---
title: HCDD 340 — Assignment 03
lang: en
date-meta: 2025-10-03
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

For this assignment, you will create a progressive web app (PWA) with JS event handling. Please use the starter file in Canvas (Files → Assignments → [Assignment-03](https://psu.instructure.com/courses/2416260/files/folder/Assignments/Assignment-03)). 

The video below shows an implementation of the assignment:

<figure>
<div class="iframe-wrapper">
<video controls muted autoplay width="600">
    <source src="media/hcdd-340-assignment-03.webm" type="video/webm" />
    <source src="media/hcdd-340-assignment-03.mp4" type="video/mp4" />
    <p>
        Your browser doesn't support HTML video. Here is a
        <a href="media/hcdd-340-assignment-03.mp4" download="hcdd-340-assignment-03.mp4">link to the video</a> instead.
    </p>
</video>
</div>
</figure>
</section>

<section>

## Deliverables
Please upload the following files (as a zip file):

* A screen recording (video) of the app showing event handling (similar to the video above).
* Your **code folder**. For grading, we will open the `index.html` in VS Code. The uploaded folder must be self-contained — please make sure that there is no error when loading `index.html` in VS Code.

</section>

<section>

## Requirements & Rubrics

### PWA
* The PWA is installable using Chrome (**5 points**)

* The app has a "standalone" [display](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/display#standalone) (**1 point**)

* The app background color is Pugh blue (`#96BEE6`) (**1 point**)

### Event handling
* Each `<a>` element within `<nav>` has a click event handler (**2 point**)

* Event handler function uses arrow (`=>`) syntax (**1 points**)

* When clicked, the color of the element is toggled between orange (`#E98300`) and purple (`#491D70`) (**6 points**)
</section>

<section>
## Implementation suggestions

### Installing PWA
* **Requirements for installing a PWA using Chrome**
    + You can see the requirements for installing a PWA using Chrome [here](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable#installability). Please note that installation isn't allowed using the `file://` protocol. We will open your project in Live Preview using VS Code and then will use the URL in Chrome for installation. You can use the same steps for development and testing.

* **Icons**
    + You will need different sized icons. You can use any [Penn State logo](https://brand.psu.edu/visual-identity-standards/) for the assignment (resize it as necessary).

* Check **Dev Tools → Application**
    + You can check issues related to installation by going to Chrome Dev Tools → Application → Manifest.

### Event handling

* **Use `defer` for loading JS script**
    + It is important to make sure that DOM is fully parsed before you try to attach any event handlers. You can use [`defer`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLScriptElement/defer) to ensure that the script is executed after the DOM is parsed (e.g., ` <script defer src="main.js"></script>`). More details [here](https://javascript.info/script-async-defer) and [here](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script#async_and_defer). What happens if you don't use `defer`?


* **Attaching event handlers to `<a>` elements**
    + Note that [`querySelector`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector) returns the _first_ matching element. Given the assignment requires event handlers for multiple elements, it might be useful to take a look at [`querySelectorAll`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll).

* **Checking current color of an element**
    + The assignment requires toggling color after a click. This means you will have to determine the current color for a given element. The following code segment can extract color information (in hex) for a given element:

```js
/**
 * Converts an RGB or RGBA color string to its hexadecimal equivalent.
 */
function rgbStringToHex(rgbString) {
  // Regex to match rgb() or rgba() strings with number or percentage values,
  // separated by spaces or commas. It captures up to four numeric groups.
  const regex = /rgba?\((\d+)[,\s]+(\d+)[,\s]+(\d+)[,\s/]*([\d.]+)?\)/i;
  const match = regex.exec(rgbString);

  if (!match) {
    return null; // Return null for invalid input
  }

  // Extract color components from the regex match
  const [r, g, b, a] = match.slice(1).map(Number);

  // Helper function to convert a number to a two-digit hex string
  const toHex = (c) => c.toString(16).padStart(2, '0');

  // Convert RGB components to hex and join them
  const hex = `${toHex(r)}${toHex(g)}${toHex(b)}`;

  // If an alpha value exists, convert it to a two-digit hex and append it
  const hexAlpha = a !== undefined && !isNaN(a) ? toHex(Math.round(a * 255)) : '';

  return `#${hex}${hexAlpha}`;
}

/**
 * Gets color (in Hex) for a given element
 */
const getTextColor = (element) => {
    const computedStyle = window.getComputedStyle(element);
    const textColor = computedStyle.getPropertyValue("color");
    return rgbStringToHex(textColor);
}
```

</section>
