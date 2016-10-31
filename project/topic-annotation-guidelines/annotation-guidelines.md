Guidelines for annotating entries
=================================

This is a living document about our annotation of repository entries with ontology terms.

General outlook to keep in mind
-------------------------------

The purpose of these annotations is to identify what the software offers to users: the features it possesses, the topics it deals with, the way that it's meant to be used, and so on.  The following is a template description that shows how different annotation aspects fit into the overall picture:

> **[name]** is **[kind of software]** providing **[functionality]** applicable to **[topics]**. It provides **[interfaces]**, supports **[data formats]**, and runs on **[OS]**. Its licensing terms reference **[licenses]**.

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

* `Library or component software`: Software that is not runnable as-is, and must be incorporated into other software or framework.  Unlike `standalone software`, library or component software must be incorporated into *other* software, framework, or *something*, and it is the "something else" that drives or runs the execution of the software.  Library and component software lacks a "main" routine and other elements that would permit the software to run on a computer or inside a web browser. The canonical example is an API library like *libc*, but this category also includes things like plug-ins for web frameworks such as *jQuery*. Also included here are toolboxes for MATLAB and packages for environments such as R, because these are almost never standalone software packages (but in the rare cases when they *are*, they should *also* be tagged with `User software`.)

* `Standalone software`: an executable application; something that can be run by itself or as part of another system.  The distinguishing feature is that it's runnable directly, unlike library or component software which must be integrated into something else.

    * `User software`: anything the user can run directly on a computer or in a web browser. Examples include a text editor running on a desktop computer, web applications with a definable purpose running in a browser, product engineering software, office applications, media players, etc.  The size or scope does not enter into the equation here: whether it runs on a desktop, or a mobile device, or as a web app, it's still standalone user software from this perspective.

    * `Infrastructure software`: software that users do not normally interact with directly except perhaps to start them or configure them. Often this software runs continuously or in the background. Examples: server-side software such as mail servers, system daemons, and operating systems. Note that it is possible for a project or repository to contain both user software and infrastructure software at the same time, when a project includes both server-side and client-side elements.

    * `Embedded software`: software that is designed to be embedded in a hardware system and interact with hardware controls.  An example is firmware meant to be loaded onto some hardware platform such as an instrument.  Another example is software that is meant to be loaded onto an Arduino board; the way such software is used and executed is markedly different from how desktop, mobile or other applications are used.  Often, embedded software does not have a software-based user interface and instead, users interact with it through hardware-based interfaces such as buttons, knobs, and lights.

It may seem as though it should be possible to infer the kind of software from the interfaces it provides.  For instance, if it offers a GUI, wouldn't it be an application?  Unfortunately, no: a library of GUI widgets would be considered `Library or component software` and not an application.  Conversely, the presence of an API does not preclude something being `Standalone software`.  An example is a MATLAB toolbox: typically, MATLAB toolboxes typically offer interfaces so that users can intearct with them, but the user executes the software by running the environment (MATLAB).

### Some specific case examples

* `rafrombrc/bm.gallery` is a media gallery built on top of Django.  In this particular case, the software is executed by running Django itself: it is not a standalone program.  Therefore, it is properly a `Library or component software`.

* `nextinterfaces/countries-app` is an app for viewing countries of the world on tablets.  This is `User software` and not `Embedded software` because when it runs on a tablet, it does not run on the bare hardware.  (Tablets are more akin to portable computers than embedded hardware systems, and generally, the only thing that qualifies as embedded software in the case of tablets is something like replacement firmware.)

* `beercanlah/ardumashtun` is software to be loaded onto an Arduino board, to control a beer brewing aparatus.  It is `Embedded software`.

* `jws85/Vintage` is a set of keymaps for the Sublime Text editor to emulate `vi`.  Should it be tagged with `hardware user interface`?  This almost seems like a yes, except that this software largely does not itself interact with the hardware: it's a set of configuration commands for a program that does.  (Admittedly a thin distinction.  Possibly worth revisiting.)


The "interfaces" annotation
---------------------------

This is meant to capture the interfaces offered by the software to users, both human users as well as other software.  By "the software", we mean the finished "product" that the source code represents.  If the eventual "product" is an application (after being compiled), then what does the application provide to users, either directly via user interaction or indirectly through the software's operation?  If it's a programming library, then what does the library provide to programmers?

Note that these are not mutually exclusive: some software offers both a UI and an API.  Some software is meant to be used directly by users (in which case, it have a UI), and some software is meant to be programmed to (in which case, it will have an API of some kind), and some software projects have multiple pieces, with elements of each.  Also note that the build system interface should in most cases *not* be considered in these annotations (or else, everything with a makefile would have a `batch interface` annotation!).  Some examples below will hopefully help clarify things.

There are two top-level divisions in our interfaces ontology: *UI* and *API*.  Most of the terms hopefully are self-explanatory, but here are explanations for some terms that may be less obvious.

### *UI*

* `hardware user interface`: This is for software that interacts with specialized hardware user interfaces &ndash; control panels with buttons and knobs, game consoles, musical instruments, or something like a [SpaceExplorer](https://www.amazon.com/connexion-SpaceExplorer-Navigation-Interface-3DX-700026/dp/B000LB5IXC) 3D navigation interface.  An important question is whether something loaded onto a smartphone (like an app for an Android phone) should be considered to have a hardware user interface in this sense.  In most cases the answer is "no", because most phone apps use a combination of `mobile graphical user interface` and `touch user interface`.

* `batch interface`: This is for software that is operated by writing instructions in a file (often, a configuration file) which the software reads in order to determine what to do.  Note that the use of a Makefile or other build system scripts or configuration files should not count as batch interfaces per se: the build system is not usually what the user of the software normally interacts with.  Some exceptional cases may arise; for instance, if the software is meant to be run as part of a build process (e.g., some sort of extension to `ant` or whatever), then it might be appropriate to tag it with `batch interface`.

* `mobile graphical user interface`: This should be self-explanatory, but note that if the software uses touch input, then it should *also* have be annotated with `touch user interface` &ndash; one does not necessarily imply the other.  (For example, some very simple mobile apps may not use touch input, and so they should only have `mobile graphical user interface`.  Also, in the past, there existed mobile devices with graphical displays that were not touchscreens.)

* `touch user interface`: Most modern smartphones and tablets today use touch-based user interfaces, so software meant for these platforms will be annotated with both `touch user interface` and (usually) `mobile graphical user interface`.  Note that touch user interfaces do not necessarily imply haptic feedback; in fact, few devices today offer haptic feedback, and even the iPhone 6 and 7 offer only partial haptic feedback.  Note also that while touch user interfaces are in some sense a kind of hardware user interface, human interaction with touchscreens is markedly different from interaction with (say) buttons on a control panel, which argues for a separate classification.  Finally, a touch interface does not imply a phone or tablet mobile device: desktop computers with touchscreens do exist.

* `pen tablet interface`: This is a separate subterm under `touch user interface` meant for devices such as Wacom graphics tablets, which require the use of a pen interface and do *not* have a graphical display.  (It is true that many pen systems exist for iPads and Android tablets, but that is not their sole or even primary mode of interaction, whereas for old-style graphics tablets, it is.)

### *API*

* `hardware`

* `function/class library interface`: This is for libraries of functions (such as the standard C library), classes (such as Java class libraries), and things such as MATLAB toolboxes.  It implies that users of the software must link their code against it, or otherwise import the library.

* `network communications interface`: This is software that is meant to be used via network interfaces of some kind.  The subterms cover specific types of network communications schemes.  

* `network sockets`: Although it is unusual to find software that uses a custom socket-based protocol rather than one of the other mechanisms below, it does happen, and in those cases, the general term `network sockets` is appropriate.  If something uses sockets but it is evident that HTTP is involved, then the annotation should be `web services interface` or one of its more specific subterms.

* `message-passing interface` is included underneath `network communications interface` instead of being a higher-level term, because all of the message-passing or message-queuing schemes use network mechanisms and can be used across multiple computers.  Some specific schemes listed here may also offer RPC or RMI mechanisms too (D-Dbus being a example), but they are listed here rather than under `RPC/RMI interface` if they are fundamentally based on message-passing.

* `web services interface` is under `RPC/RMI interface` because all of the web services are in fact a kind of remote procedure call or remote method invocation.

* Further subdivisions under `web-services interface` identify more specific mechanisms.  Usually, it's possible to tell whether something uses `SOAP` or `REST` or `Ajax` simply by searching the code for those strings of characters.  Sometimes it's evident that code uses some kind of HTTP-based interaction (e.g., because searching the code reveals identifiers with the string `http` in them, or something along those lines), but it is difficult to tell whether it's using a `REST` approach or something else.  In those cases, using the term `web services interface` is probably the best option.

An important question is what to do if something uses, say, a network interface as part of its implementation.  For instance, a number of software applications have self-update mechanisms that operate over the network.  Should they be annotated with an API term for `network communications interface`?  In almost all cases, no: these are not "interfaces offered to the user" in the intended sense.  One way to think about it is whether a user looking for the software would think about the interface.  In most cases, someone looking for some software application will probably not think about how the updating scheme is implemented.


### Some specific examples

* `fprefect/videopoker` is an example of something that its setup data from a file, and not from a command-line or GUI interface (although it is started from a command line).  This is just barely a reasonable case for annotating with `batch interface`.

* `albfernandez/GDS-PMD-Security-Rules` is another example of `batch interface`, because the behavior controlling instructions are written in files.

* `beercanlah/ardumashtun` is software to be loaded onto an Arduino board, to control a beer brewing aparatus.  It certainly has `hardware user interface` and `hardware device interface` because when it runs, it runs on the Arduino.  A more difficult question is whether the testing code in that repository warrants an annotation of `command-line interface`.  It probably does.


The "topics" annotation
------------------------

The topics annotations are meant to capture the prominent *topics* or *subjects* of a particular software source code repository.  What we want is to identify what the software is about, what the software concerns.  The range of possible topics is essentially unbounded, which is why the use of the [Library of Congress Subject Headings](http://id.loc.gov/authorities/subjects.html) as annotation terms is particularly appropriate.

Something to watch out for is how the topic annotations interact with the annotations used for the kind of software and the interfaces provided by the software.

* If the software is actually *about* something described by the interfaces ontology above, an appropriate LCSH term should be added.  For example, a library of GUI widgets should be annotated with the LCSH topics term for GUIs, which is `sh93002168` ("Graphical user interfaces") or possibly `sh2008009921` ("Web-based user interfaces") if that is more appropriate.  Similarly, if the software is a library for (say) Ajax programming, it should receive the appropriate topics term, even if it also has `interfaces` annotations for those things.

* If the software is about something specifically for a particular language such as Java or Python, the appropriate LCSH term should be added.  Since we're currently only looking at Python and Java based software, there are only two relevant terms:

    * `sh96008834`: "Python (Computer program language)"
    * `sh95008574`: "Java (Computer program language)"

* Software for Android or iOS can usually be used on both phones and tablets, and thus *normally* should receive annotations of `sh2007006251` ("Smartphones") and `sh2010009240` ("Tablet computers").  *Exception*: sometimes the software is specific to a particular model of device, or is clearly stated to be for a phone only.  In that case, we should probably annotate it only with `sh2007006251`.

* Certain terms are **not** appropriate because they are not what we think they are.  Here is a running list of terms to avoid:

    * sh88007957: `Cache Memory`: This *seems* like it would be appropriate for things like software cache systems (e.g., Redis, memcached), but this particular term is about *hardware* memory cache storage.  (The immediate hierarchy of this term goes like this: sh98003200 `Computer systems` → sh85029505 `Computer input-output equipment` → sh85029541 `Computer storage devices` → sh88007957 `Cache memory`.) It is probably inappropriate to use this for software caches.
