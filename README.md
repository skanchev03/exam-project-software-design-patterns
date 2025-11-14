# Media Library Management System

**Author:** Stefan Nikolay Kanchev

---

## Overview

This project implements a **Media Library Management System** for handling books, movies, and music. It allows users to:

- Add and remove media items
- Filter items by genre
- Rate media items

The system demonstrates the use of **Object-Oriented Design Patterns**, including **Adapter**, **Iterator**, and **Observer**, ensuring flexibility, scalability, and separation of concerns. It is implemented as a **RESTful web service** using **Flask**.

---

## Architecture

The project is organized into several modules:

- `media/` – Contains concrete media classes (`Book`, `Movie`, `Music`) and their respective adapters implementing a common interface (`MediaInterface`).
- `patterns/` – Implements design patterns: `Iterator`, `Observer`, and `MediaLibrary` (combining Iterator and Observer behavior).
- `main.py` – Flask server providing REST API for external interaction.
- `files/` – Contains resources such as UML diagrams, assignment description, and demonstration scripts.

---

## Design Patterns

### Adapter Pattern
Used to unify interfaces of different media types. Despite differences in attributes, each media class (`Book`, `Movie`, `Music`) has an adapter (`BookAdapter`, `MovieAdapter`, `MusicAdapter`) implementing `MediaInterface`.

### Iterator Pattern
Implemented via `MediaIterator`, providing sequential access to media items in `MediaLibrary`. The library implements `__iter__()` to support iteration.

### Observer Pattern
Implemented via `Subject`, `Observer`, and `MediaObserver`. `MediaLibrary` notifies observers whenever media is added or removed. `MediaObserver` prints notifications about changes.

---

## Key Interfaces and Classes

### MediaInterface
Abstract class defining required methods for all adapted media objects:

- `get_title()`
- `get_creator()`
- `get_year()`
- `get_genre()`
- `get_rating()`
- `get_details()`
- `set_rating(rating)`

### Media Types
- **Book / Movie / Music**: Represent specific media items with attributes for title, creator/author/director/artist, year, genre, and rating.  
- **Adapters**: Map each media type to `MediaInterface`.

### MediaIterator
Sequentially iterates over a list of media objects.

### MediaLibrary
Manages media objects, supports iteration and notifications. Provides methods:

- `add_media(media)`
- `remove_media(media)`
- `filter_by_genre(genre)`
- `__iter__()`

### Observer Classes
- `Subject` – Base class for objects with observers.
- `Observer` – Abstract observer class.
- `MediaObserver` – Prints notifications for added or removed media.

---

## REST API (via Flask)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/media` | Retrieve all media items |
| POST   | `/media` | Add a new media item (JSON: `type`, `title`, `genre`, `year`, `extra`) |
| GET    | `/media/genre/<genre>` | Retrieve media filtered by genre |
| POST   | `/media/<title>/rating` | Set rating for a media item |
| DELETE | `/media/<title>` | Remove a media item |

The Adapter pattern ensures all media types are accessed through a unified interface.
