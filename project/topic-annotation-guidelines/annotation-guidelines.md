Guidelines for annotating entries
=================================

This is a living document about our annotation of repository entries with ontology terms.

General outlook to keep in mind
-------------------------------

The purpose of these annotations is to identify what the software offers to users: the features it possesses, the topics it deals with, the way that it's meant to be used, and so on.  The following is a template description that shows how different annotation aspects fit into the overall picture:

<div style="font-style: italic; margin: auto 2em; color: darkgreen">
<b>[name]</b> is <b>[kind of software]</b> providing <b>[functionality]</b> applicable to <b>[topics]</b>. It provides <b>[interfaces]</b>, supports <b>[data formats]</b>, and runs on <b>[OS]</b>. Its licensing terms reference <b>[licenses]</b>.
</div>

The meanings are as follows:

* _name_: The name of the software.

* _kind of software_: Whether it's a library, or a desktop app, or something else.  Currently, this is captured by our *kind* ontology terms, discussed below.

* _functionality_: The operations supported by the software.  <span style="color: darkred">Currently, our annotations about this are mixed with the annotations for topics &ndash; something that needs to be fixed.</span>

* _topics_: The topics to which the software is applicable, such as biology topics or astronomy or similar.  We use Library of Congress Subject Heading terms, as discussed below.

* _interfaces_: The types of user interfaces and/or APIs that the software provides to users and programmers.

* _data formats_: The data formats supported for input and output.  <span style="color: darkred">(We currently don't have anything for this.)</span>

* _OS_: The operating system(s) on which the software can run.  <span style="color: darkred">(We currently don't have anything for this.)</span>

* _licenses_: The licensing terms.  We will be able to get this in part from the GitHub entries themselves, now that GitHub includes license info in the data it presents.


The "kind" annotation
----------------------

This is meant to capture how the software can be used.  Currently, we only distinguish 3 concepts:

* `application software`: A full standalone application; something a user can use directly.  The size or scope does not enter into the equation here: whether it runs on a desktop, or a mobile device, or as a web app, or *something*, it's still an application from this perspective. 

* `component software`: A library or toolbox that can be used as components; something that is *not* "runnable" by itself.  The term is "component" instead of "library" or a similar term, to encompass things such as plug-ins for web application frameworks.

* `embedded/embeddable software`: Software that is designed to be embedded in a hardware system and interact with hardware controls.  An example is firmware meant to be loaded onto some hardware platform such as a mobile phone.  Another example is software that is meant to be loaded onto an Arduino board; the way such software is used and executed is markedly different from how desktop, mobile or other applications are used.  Often, embedded software does not have a software-based user interface and instead, users interact with it through hardware-based interfaces such as buttons, knobs, and lights.

It may seem as though it should be possible to infer the kind of software from the interfaces it provides.  For instance, if it offers a GUI, wouldn't it be an application?  Unfortunately, no: a library of GUI widgets would be considered `component software` and not an application.  Conversely, the presence of an API does not preclude something being `application software`.  An example is a MATLAB toolbox: typically, MATLAB toolboxes typically offer interfaces so that users can intearct with them directly, but they can also be used as components.  Finally, a given software project can be more than one of these; MATLAB toolboxes are an example, and there are many cases of software applications that can also be used as components of other software.  In these cases, the database entry should be annotated with both terms.

The "kind" ontology currently does not divide software further.  It is tempting to subvide the 3 categories into finer distinctions such as "utilities", "mobile application", etc. (And indeed, the LCSH has terms for such things.) But finer distinctions become harder to make with certainty when inspecting software, and moreover, some of the distinctions are fundamentally arbirtrary and difficult to agree upon, such as whether something is a "utility".


The "interfaces" annotation
---------------------------

This is meant to capture the interfaces offered by the software to users, both human users as well as other software.  When adding or reading this annotation, the point of view to keep in mind is that it is *not* the interfaces that the software may use to implement its functionality, but rather, *what it provides to users*.  Some software is meant to be used directly by users (in which case, it have a UI), and some software is meant to be programmed to (in which case, it will have an API of some kind).  Note that these are not mutually exclusive: some software offers both a UI and an API.  Also note that the build system interface should in most cases not be considered in these annotations (or else, everything with a makefile would have a `batch interface` annotation!).  Some examples below will hopefully help clarify things.

There are two top-level divisions in our interfaces ontology: *UI* and *API*.  Most of the terms hopefully are self-explanatory, but here are explanations for some terms that may be less obvious.

### *UI*

* `hardware user interface`: This is for software that interacts with specialized hardware user interfaces &ndash; control panels with buttons and knobs, game consoles, musical instruments, or something like a [SpaceExplorer](https://www.amazon.com/connexion-SpaceExplorer-Navigation-Interface-3DX-700026/dp/B000LB5IXC) 3D navigation interface.  An important question is whether something loaded onto a smartphone (like an app for an Android phone) should be considered to have a hardware user interface in this sense.  In most cases the answer is "no", because most phone apps use a combination of `mobile graphical user interface` and `touch user interface`.

* `batch interface`: This is for software that is operated by writing instructions in a file (often, a configuration file) which the software reads in order to determine what to do.  Note that the use of a Makefile or other build system scripts or configuration files should not count as batch interfaces per se: the build system is not usually what the user of the software normally interacts with.  An exception can arise if the software is actually a tool for developers.  In that case, if the software has configuration scripts for driving it, then it would be appropriate to tag it with `batch interface` if that is how users of the software (i.e., other developers) interact with it.

* `mobile graphical user interface`: This should be self-explanatory, but note that if the software uses touch input, then it should *also* have be annotated with `touch user interface` &ndash; one does not necessarily imply the other.  (For example, some very simple mobile apps may not use touch input, and so they should only have `mobile graphical user interface`.  Also, in the past, there existed mobile devices with graphical displays that were not touchscreens.)

* `touch user interface`: Most modern smartphones and tablets today use touch-based user interfaces, so software meant for these platforms will be annotated with both `touch user interface` and (usually) `mobile graphical user interface`.  Note that touch user interfaces do not necessarily imply haptic feedback; in fact, few devices today offer haptic feedback, and even the iPhone 6 and 7 offer only partial haptic feedback.  Note also that while touch user interfaces are in some sense a kind of hardware user interface, human interaction with touchscreens is markedly different from interaction with (say) buttons on a control panel, which argues for a separate classification.  Finally, a touch interface does not imply a phone or tablet mobile device: desktop computers with touchscreens do exist.

* `pen tablet interface`: This is a separate subterm under `touch user interface` meant for devices such as Wacom graphics tablets, which require the use of a pen interface and do *not* have a graphical display.  (It is true that many pen systems exist for iPads and Android tablets, but that is not their sole or even primary mode of interaction, whereas for old-style graphics tablets, it is.)

### *API*

* `function/class library interface`: This is for libraries of functions (such as the standard C library), classes (such as Java class libraries), and things such as MATLAB toolboxes.  It implies that users of the software must link their code against it, or otherwise import the library.

* `network communications interface`: This is software that is meant to be used via network interfaces of some kind.  The subterms cover specific types of network communications schemes.  

* `network sockets`: Although it is unusual to find software that uses a custom socket-based protocol rather than one of the other mechanisms below, it does happen, and in those cases, the general term `network sockets` is appropriate.  If something uses sockets but it is evident that HTTP is involved, then the annotation should be `web services interface` or one of its more specific subterms.

* `message-passing interface` is included underneath `network communications interface` instead of being a higher-level term, because all of the message-passing or message-queuing schemes use network mechanisms and can be used across multiple computers.  Some specific schemes listed here may also offer RPC or RMI mechanisms too (D-Dbus being a example), but they are listed here rather than under `RPC/RMI interface` if they are fundamentally based on message-passing.

* `web services interface` is under `RPC/RMI interface` because all of the web services are in fact a kind of remote procedure call or remote method invocation.

* Further subdivisions under `web-services interface` identify more specific mechanisms.  Usually, it's possible to tell whether something uses `SOAP` or `REST` or `Ajax` simply by searching the code for those strings of characters.  Sometimes it's evident that code uses some kind of HTTP-based interaction (e.g., because searching the code reveals identifiers with the string `http` in them, or something along those lines), but it is difficult to tell whether it's using a `REST` approach or something else.  In those cases, using the term `web services interface` is probably the best option.

An important question is what to do if something uses, say, a network interface as part of its implementation.  For instance, a number of software applications have self-update mechanisms that operate over the network.  Should they be annotated with an API term for `network communications interface`?  In almost all cases, no: these are not "interfaces offered to the user" in the intended sense.  One way to think about it is whether a user looking for the software would think about the interface.  In most cases, someone looking for some software application will probably not think about how the updating scheme is implemented.


The "topics" annotation
------------------------

The topics annotations are meant to capture the prominent *topics* or *subjects* of a particular software source code repository.  What we want is to identify what the software is about, what the software concerns.  The range of possible topics is essentially unbounded, which is why the use of the [Library of Congress Subject Headings](http://id.loc.gov/authorities/subjects.html) as annotation terms is particularly appropriate.

Something to watch out for is how the topic annotations interact with the annotations used for the kind of software and the interfaces provided by the software.

* If the software is actually *about* something described by the interfaces ontology above, an appropriate LCSH term should be added.  For example, a library of GUI widgets should be annotated with the LCSH topics term for GUIs, which is `sh93002168` ("Graphical user interfaces") or possibly `sh2008009921` ("Web-based user interfaces") if that is more appropriate.  Similarly, if the software is a library for (say) Ajax programming, it should receive the appropriate topics term, even if it also has `interfaces` annotations for those things.
