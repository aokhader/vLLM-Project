import json
import time
import threading


def display_timer(start_time: float, stop_event: threading.Event) -> None:
    """
    Display a live timer in the console.
    :param start_time: Time when the timer started.
    :param stop_event: Event to signal when to stop the timer.
    :return: None
    """
    while not stop_event.is_set():
        elapsed = int(time.time() - start_time)
        hours = elapsed // 3600
        minutes = (elapsed % 3600) // 60
        seconds = elapsed % 60
        print(
            f"\rElapsed Time: {hours:02d}:{minutes:02d}:{seconds:02d}",
            end="",
            flush=True,
        )
        time.sleep(1)
    # Clear the timer line when done
    print("\r" + " " * 50 + "\r", end="", flush=True)


def load_jsonl(file_path: str, limit: int = None) -> list:
    """
    Load a JSONL file into a list of dictionaries.
    :param file_path: Path to the JSONL file.
    :param limit: Optional limit on the number of lines to read.
    :return: List of dictionaries loaded from the JSONL file.
    """
    data = []
    with open(file_path, "r") as file:
        for i, line in enumerate(file):
            if limit and i >= limit:
                break
            data.append(json.loads(line))
    return data


def count_review_images(reviews: list) -> tuple:
    """
    Count reviews that have images.
    :param reviews: List of review dictionaries.
    :return: Tuple of (total reviews, reviews with images).
    """
    total = len(reviews)
    with_images = sum(
        1 for r in reviews if isinstance(r.get("images"), list) and len(r["images"]) > 0
    )
    return total, with_images


def count_metadata_images(metadata: list) -> tuple:
    """
    Count metadata items that have images.
    :param metadata: List of metadata dictionaries.
    :return: Tuple of (total items, items with images).
    """
    total = len(metadata)
    with_images = sum(1 for m in metadata if m.get("images"))
    return total, with_images


def count_items_with_both(reviews: list, metadata: list) -> int:
    """
    Count items that have images in both reviews and metadata.
    :param reviews: List of review dictionaries.
    :param metadata: List of metadata dictionaries.
    :return: Count of items with images in both reviews and metadata.
    """
    meta_map = {m.get("parent_asin"): m for m in metadata if m.get("parent_asin")}
    count = 0

    for r in reviews:
        parent = r.get("parent_asin")
        if not parent:
            continue

        review_has_images = isinstance(r.get("images"), list) and len(r["images"]) > 0
        meta = meta_map.get(parent)
        metadata_has_images = meta and meta.get("images")

        if review_has_images and metadata_has_images:
            count += 1

    return count


def print_summary_table(
    total_reviews: int,
    review_with_images: int,
    total_metadata: int,
    metadata_with_images: int,
    both_count: int,
) -> None:
    """
    Prints a summary table of image coverage statistics.
    :param total_reviews: Total number of reviews.
    :param review_with_images: Number of reviews with images.
    :param total_metadata: Total number of metadata items.
    :param metadata_with_images: Number of metadata items with images.
    :param both_count: Number of items with images in both reviews and metadata.
    :return: None
    """
    print("\n==============================================")
    print("         IMAGE COVERAGE SUMMARY       ")
    print("==============================================")
    print(f"{'Metric':35} | {'Count'}")
    print("----------------------------------------------")
    print(f"{'Total reviews':35} | {total_reviews}")
    print(f"{'Reviews with images':35} | {review_with_images}")
    print(f"{'% Reviews with images':35} | {review_with_images / total_reviews:.2%}")
    print("----------------------------------------------")
    print(f"{'Total metadata items':35} | {total_metadata}")
    print(f"{'Metadata items with images':35} | {metadata_with_images}")
    print(
        f"{'% Metadata with images':35} | {metadata_with_images / total_metadata:.2%}"
    )
    print("----------------------------------------------")

    # New percentage for items with BOTH
    both_pct = both_count / total_reviews

    print(f"{'Items with BOTH review + metadata images':35} | {both_count}")
    print(f"{'% BOTH (vs all reviews)':35} | {both_pct:.2%}")

    print("==============================================\n")


def main():
    DATASET_SIZE = 500_000

    # Update these paths
    reviews_path = "../datasets/review/Clothing_Shoes_and_Jewelry.jsonl"
    metadata_path = "../datasets/metadata/meta_Clothing_Shoes_and_Jewelry.jsonl"

    print("Loading data...")
    print("=" * 46)
    print(f"  Reviews: Clothing_Shoes_and_Jewelry")
    print(f"  Metadata: meta_Clothing_Shoes_and_Jewelry")
    print("=" * 46)
    print()
    start_time = time.time()

    # Start the timer thread
    stop_event = threading.Event()
    timer_thread = threading.Thread(target=display_timer, args=(start_time, stop_event))
    timer_thread.start()

    reviews = load_jsonl(reviews_path, DATASET_SIZE)
    metadata = load_jsonl(metadata_path, DATASET_SIZE)

    print("\n\nProcessing...")

    # # Compute counts
    total_reviews, review_with_images = count_review_images(reviews)
    total_metadata, metadata_with_images = count_metadata_images(metadata)
    both_count = count_items_with_both(reviews, metadata)

    # # Print summary table
    print_summary_table(
        total_reviews,
        review_with_images,
        total_metadata,
        metadata_with_images,
        both_count,
    )

    # Stop the timer
    stop_event.set()
    timer_thread.join()


if __name__ == "__main__":
    main()
