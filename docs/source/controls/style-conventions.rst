Style Guide
====

Source: Google Java Style Guide<Google Java Style Guide>

Block indentation: +2 spaces Each time a new block or block-like construct is opened, the indent increases by two spaces. When the block ends, the indent returns to the previous indent level. The indent level applies to both code and comments throughout the block. (See the example in Section 4.1.2, Nonempty blocks: K & R Style.)

4.3 One statement per line Each statement is followed by a line break.

4.4 Column limit: 100 Java code has a column limit of 100 characters. A "character" means any Unicode code point. Except as noted below, any line that would exceed this limit must be line-wrapped, as explained in Section 4.5, Line-wrapping.

Each Unicode code point counts as one character, even if its display width is greater or less. For example, if using fullwidth characters, you may choose to wrap the line earlier than where this rule strictly requires.

Exceptions:

Lines where obeying the column limit is not possible (for example, a long URL in Javadoc, or a long JSNI method reference). package and import statements (see Sections 3.2 Package statement and 3.3 Import statements). Command lines in a comment that may be copied-and-pasted into a shell. Very long identifiers, on the rare occasions they are called for, are allowed to exceed the column limit. In that case, the valid wrapping for the surrounding code is as produced by google-java-format. 4.5 Line-wrapping Terminology Note: When code that might otherwise legally occupy a single line is divided into multiple lines, this activity is called line-wrapping.

There is no comprehensive, deterministic formula showing exactly how to line-wrap in every situation. Very often there are several valid ways to line-wrap the same piece of code.

Note: While the typical reason for line-wrapping is to avoid overflowing the column limit, even code that would in fact fit within the column limit may be line-wrapped at the author's discretion.

Tip: Extracting a method or local variable may solve the problem without the need to line-wrap.

4.5.1 Where to break The prime directive of line-wrapping is: prefer to break at a higher syntactic level. Also:

When a line is broken at a non-assignment operator the break comes before the symbol. (Note that this is not the same practice used in Google style for other languages, such as C++ and JavaScript.) This also applies to the following "operator-like" symbols: the dot separator (.) the two colons of a method reference (::) an ampersand in a type bound (<T extends Foo & Bar>) a pipe in a catch block (catch (FooException | BarException e)). When a line is broken at an assignment operator the break typically comes after the symbol, but either way is acceptable. This also applies to the "assignment-operator-like" colon in an enhanced for ("foreach") statement. A method or constructor name stays attached to the open parenthesis (() that follows it. A comma (,) stays attached to the token that precedes it. A line is never broken adjacent to the arrow in a lambda, except that a break may come immediately after the arrow if the body of the lambda consists of a single unbraced expression. Examples: MyLambda<String, Long, Object> lambda = (String label, Long value, Object obj) -> { ... };

Predicate predicate = str -> longExpressionInvolving(str); Note: The primary goal for line wrapping is to have clear code, not necessarily code that fits in the smallest number of lines.

4.5.2 Indent continuation lines at least +4 spaces When line-wrapping, each line after the first (each continuation line) is indented at least +4 from the original line.

When there are multiple continuation lines, indentation may be varied beyond +4 as desired. In general, two continuation lines use the same indentation level if and only if they begin with syntactically parallel elements.

Section 4.6.3 on Horizontal alignment addresses the discouraged practice of using a variable number of spaces to align certain tokens with previous lines.