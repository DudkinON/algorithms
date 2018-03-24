"""
Gets amount of segments and segments like:
4       <- amount of segments
4 7     <- segments [4 .... 7] etc
1 3
2 5
5 6

Then print amount of dots and dots which covered all segments like:
2       <- amount of dots
3 6     <- list of dots
"""
from operator import itemgetter


def cover(segments):
    counter = 0
    answer = []
    for segment in sorted(segments, key=itemgetter(1)):
        if len(answer):
            if answer[-1] < int(segment[0]):
                answer.append(int(segment[1]))
                counter += 1
        else:
            answer.append(int(segment[1]))
            counter += 1
    print counter
    return answer


def main():
    segments = []
    for i in range(int(raw_input())):
        segments.append(raw_input().split())
    print ' '.join(str(v) for v in cover(segments))


if __name__ == "__main__":
    main()
