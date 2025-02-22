trait Animal {
    fn speak(&self);
}

struct Dog;

impl Animal for Dog {
    fn speak(&self) {
        println!("Howl!")
    }
}

struct Cat;

impl Animal for Cat {
    fn speak(&self) {
        println!("Meow!")
    }
}

fn animal_speak<T: Animal>(animal: T) {
    animal.speak();
}

fn main() {
    animal_speak(Dog {});
    animal_speak(Dog {});
    animal_speak(Cat {});
}