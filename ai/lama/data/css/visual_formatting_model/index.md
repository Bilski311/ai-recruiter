---
title: Visual formatting model
slug: Web/CSS/Visual_formatting_model
page-type: guide
---

{{CSSRef}}

In CSS The **Visual Formatting Model** describes how user agents take the document tree, and process and display it for visual media. This includes {{glossary("continuous media")}} such as a computer screen and [paged media](/en-US/docs/Web/CSS/Paged_Media) such as a book or document printed by browser print functions. Most of the information applies equally to continuous and paged media.

In the visual formatting model, each element in the document tree generates zero or more boxes according to the box model. The layout of these boxes is governed by:

- Box dimensions and type.
- Positioning scheme (normal flow, float, and absolute positioning).
- Relationships between elements in the document tree.
- External information (e.g., viewport size, intrinsic dimensions of images, etc.).

Much of the information about the visual formatting model is defined in CSS2, however, various level 3 specifications have added to this information. When reading specifications you will often find references to the model as defined in CSS2, so an understanding of the model and the terms used to describe it in CSS2 is valuable when reading other layout specifications.

In this document we define the model and introduce some of the related terms and concepts, linking to more specific pages on MDN for further details.

## The role of the viewport

In continuous media, the {{glossary("viewport")}} is the viewing area of the browser window. User agents can change the layout of the page when the viewport size changes — for example, if you resize your window, or change the orientation of a mobile device.

If the viewport is smaller than the size of the document then the user agent needs to offer a way to scroll to the parts of the document that are not displayed. We most often see this as scrolling in the **block dimension** — vertically in a horizontal, top-to-bottom language. However, you might design something that requires scrolling in the **inline dimension** too.

## Box generation

**Box generation** is the part of the CSS visual formatting model that creates boxes from the document's elements. Generated boxes are of different types, which affect their visual formatting. The type of the box generated depends on the value of the CSS {{cssxref("display")}} property.

Initially defined in CSS2, the `display` property is extended in the [CSS Display Module Level 3](https://www.w3.org/TR/css-display-3/). In addition, some of the terminologies around the display have been updated and clarified in the years since CSS2.

CSS takes your source document and renders it onto a canvas. To do this, it generates an intermediary structure, the **box tree**, which represents the formatting structure of the rendered document. Each box in the box tree represents its corresponding element (or pseudo-element) in space and/or time on the canvas, while each text run in the box tree likewise represents the contents of its corresponding text nodes.

Then, for each element, CSS generates zero or more boxes as specified by that element's `display` property value.

> **Note:** Boxes are often referred to by their display type — e.g. a box generated by an element with `display: block` is called a "block box" or just a "block". Note however that block boxes, block-level boxes and box containers are all subtly different; see the [Block boxes](#block_boxes) section below for more details.

### The principal box

When an element generates one or more boxes, one of them is the **principal box**, which contains its descendant boxes and generated content in the box tree, and is also the box involved in any positioning scheme.

Some elements may generate additional boxes in addition to the principal box, for example `display: list-item` generates more than one box (e.g. a **principal block box** and a **child marker box**). And some values (such as `none` or `contents`) cause the element and/or its descendants to not generate any boxes at all.

### Anonymous boxes

An **anonymous box** is created when there is not an HTML element to use for the box. This situation happens when, for example, you declare `display: flex` on a parent element, and directly inside there is a run of text not contained in another element. In order to fix the box tree, an anonymous box is created around that run of text. It will then behave as a flex item, however, it cannot be targeted and styled like a regular box because there is no element to target.

{{EmbedGHLiveSample("css-examples/visual-formatting/anonymous-flex.html", '100%', 720)}}

The same thing happens when you have text runs interspersed with block elements. In the next example I have a string inside a `<div>`; in the middle of my string is a `<p>` element containing part of the text.

{{EmbedGHLiveSample("css-examples/visual-formatting/anonymous-block.html", '100%', 720)}}

The string is split into three boxes in the box tree. The part of the string before the paragraph element is wrapped in an anonymous box, then we have the `<p>`, which generates a box, and then another anonymous box.

Something to consider about these anonymous boxes is that they inherit styles from their direct parent, but you cannot change how they look by targeting the anonymous box. In my examples, I am using a direct child selector to target the children of the container. This does not change the anonymous boxes, as they are not "elements" as such.

**Inline anonymous boxes** are created when a string is split by an inline element, for example, a sentence that includes a section wrapped with `<em></em>`. This splits the sentence into three inline boxes — an anonymous inline box before the emphasized section, the section wrapped in the `<em>` element, then a final anonymous inline box. As with the anonymous block boxes, these anonymous inline boxes cannot be styled independently in the way the `<em>` can; they just inherit the styles of their container.

Other formatting contexts also create anonymous boxes. [Grid Layout](/en-US/docs/Web/CSS/CSS_Grid_Layout) behaves in the same way as the [flexbox](/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout) example above, turning strings of text into a grid item with an anonymous box. [Multiple-column](/en-US/docs/Web/CSS/CSS_Columns) layout creates anonymous column boxes around the columns; these also cannot be styled or otherwise targeted. [Table layout](/en-US/docs/Web/CSS/CSS_Table) will add anonymous boxes to create a proper table structure — for example adding an anonymous table row — if there was no box with `display: table-row`.

### Line boxes

**Line boxes** are the boxes that wrap each line of text. You can see the difference between line boxes and their containing block if you float an item and then follow it by a block that has a background color.

In the following example, the line boxes following the floated `<div>` are shortened to wrap around the float. The background of the box runs behind the float, as the floated item has been taken out of flow.

{{EmbedGHLiveSample("css-examples/visual-formatting/line-boxes.html", '100%', 720)}}

## Positioning schemes and in-flow and out-of-flow elements

In CSS, a box may be laid out according to three positioning schemes — **normal flow**, **floats**, or **absolute positioning**.

### Normal flow

In CSS, the normal flow includes block-level formatting of block boxes, inline-level formatting of inline boxes, and also includes relative and sticky positioning of block-level and inline-level boxes.

Read more about [flow layout](/en-US/docs/Web/CSS/CSS_Flow_Layout) in CSS.

### Floats

In the float model, a box is first laid out according to the normal flow, then taken out of the flow and positioned, typically to the left or right. Content may flow along the side of a float.

Find out more about [floats](/en-US/docs/Learn/CSS/CSS_layout/Floats).

### Absolute positioning

In the absolute positioning model (which also includes fixed positioning), a box is removed from the normal flow entirely and assigned a position with respect to a containing block (which is the viewport in the case of fixed positioning).

An element is called **out of flow** if it is floated, absolutely positioned, or is the root element. An element is called **in-flow** if it is not out of the flow.

Read about [CSS Positioned Layout](/en-US/docs/Web/CSS/CSS_Positioning).

## Formatting contexts and the display property

Boxes can be described as having an **outer display type**, which is `block` or `inline`. This outer display type refers to how the box behaves alongside other elements on the page.

Boxes also have an inner display type, dictating how their children behave. For normal block and inline layout, or normal flow, this display type is `flow`. This means that the child elements will also be either `block` or `inline`.

However, the inner display type might be something like `grid` or `flex`, in which case the direct children will display as a grid, or flex items. In such a case the element is described as creating a grid or flex [formatting context](/en-US/docs/Web/CSS/CSS_Flow_Layout/Intro_to_formatting_contexts). In many ways this is similar to a block formatting context, however, the children behave as flex or grid items rather than items in normal flow.

The interactions between block-level and inline-level boxes are described in the MDN documentation for {{cssxref("display")}}.

In addition, the references for specific values of display explain how these formatting contexts work in terms of box layout.

- [CSS Grid Layout](/en-US/docs/Web/CSS/CSS_Grid_Layout)
- [CSS Flexible Box Layout](/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout)
- [CSS Table Layout](/en-US/docs/Web/CSS/CSS_Table)
- [Lists](/en-US/docs/Web/CSS/CSS_Lists_and_Counters)

### Independent formatting contexts

Elements either participate in the formatting context of their containing block or establish an independent formatting context. A grid container, for example, establishes a new **Grid Formatting Context** for its children.

**Independent formatting contexts** contain floats, and margins do not collapse across formatting context boundaries. Therefore, creating a new block formatting context can ensure that floats and margins remain inside a box. To do this, add `display: flow-root` to the box on which you wish to create a new [block formatting context](/en-US/docs/Web/Guide/CSS/Block_formatting_context).

The following example shows the effect of `display: flow-root`. The box with the black background appears to wrap round the floated item and text. If you remove `display: flow-root` from the editable CSS the floated item will poke out of the bottom of the box as it is no longer contained.

{{EmbedGHLiveSample("css-examples/display/multi-keyword/block-flow-root.html", '100%', 720)}}

### Block boxes

In specifications, block boxes, block-level boxes, and block containers are all referred to as **block boxes** in certain places. These things are somewhat different and the term block box should only be used if there is no ambiguity.

#### Block containers

A **block container** either contains only inline-level boxes participating in an inline formatting context, or only block-level boxes participating in a block formatting context. For this reason, we see the behavior explained above, where anonymous boxes are introduced to ensure all of the items can participate in a block or inline formatting context. An element is a block container only if it contains block-level or inline-level boxes.

#### Inline-level and block-level boxes

These are the boxes contained inside the block container that are participating in inline or block layout, respectively.

#### Block boxes

A block box is a block-level box that is also a block container. As described in CSS `display`, it is possible for a box to be a block-level box, but not also a block container (it might be a flex or grid container for example).

## See also

- CSS key concepts:
  - [CSS syntax](/en-US/docs/Web/CSS/Syntax)
  - [Comments](/en-US/docs/Web/CSS/Comments)
  - [Specificity](/en-US/docs/Web/CSS/Specificity)
  - [Inheritance](/en-US/docs/Web/CSS/inheritance)
  - [Box model](/en-US/docs/Web/CSS/CSS_Box_Model/Introduction_to_the_CSS_box_model)
  - [Layout modes](/en-US/docs/Web/CSS/Layout_mode)
  - **Visual formatting models**
  - [Margin collapsing](/en-US/docs/Web/CSS/CSS_Box_Model/Mastering_margin_collapsing)
  - Values
    - [Initial values](/en-US/docs/Web/CSS/initial_value)
    - [Computed values](/en-US/docs/Web/CSS/computed_value)
    - [Used values](/en-US/docs/Web/CSS/used_value)
    - [Actual values](/en-US/docs/Web/CSS/actual_value)
  - [Value definition syntax](/en-US/docs/Web/CSS/Value_definition_syntax)
  - [Shorthand properties](/en-US/docs/Web/CSS/Shorthand_properties)
  - [Replaced elements](/en-US/docs/Web/CSS/Replaced_element)