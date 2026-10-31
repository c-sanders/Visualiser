#! /bin/bash

TIME_OPERATION=true
TIME_OPERATION_NO_ENCODING=true

FFMPEG="/usr/bin/ffmpeg"
FILE_LIST="file_list_output.txt"

OUTPUT_FILE="output.mp4"

OPERATION="create_animation_optimised"


# Original command

# "${FFMPEG}" -y \
#           -f concat \
#           -safe 0 \
#           -i "${FILE_LIST}" \
#           -framerate 30 \
#           -vf "pad=width=ceil(iw/2)*2:height=ceil(ih/2)*2" \
#           -c:v libx264 \
#           -pix_fmt yuv420p \
#           ${OUTPUT_FILE}

# "${FFMPEG}" -y \
#     -f concat \
#     -safe 0 \
#     -i "${FILE_LIST}" \
#     -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" \
#     -r 30 \
#     -c:v libx264 \
#     -pix_fmt yuv420p \
#     -crf 18 \
#     "${OUTPUT_FILE}"

case "$OPERATION" in

    time_no_encoding)

        /usr/bin/time -v \
        "${FFMPEG}" -y \
        -threads 1 \
        -framerate 10 \
        -start_number 0 \
        -i "rotation-%04d.png" \
        -f null -

        ;;

    time_no_encoding_zero_latency)

        /usr/bin/time -v \
        "${FFMPEG}" -y \
        -framerate 10 \
        -start_number 0 \
        -i "rotation-%04d.png" \
        -c:v libx264 \
        -pix_fmt yuv420p \
        -preset ultrafast \
        -tune zerolatency \
        -x264-params "threads=1:rc-lookahead=0" \
        output.mp4

        ;;

    time_control_video_encoder)

        /usr/bin/time -v \
        "${FFMPEG}" -y \
        -threads 1 \
        -framerate 10 \
        -start_number 0 \
        -i "rotation-%04d.png" \
        -c:v libx264 \
        -threads:v 1 \
        -pix_fmt yuv420p \
        -preset ultrafast \
        -tune zerolatency \
        -x264-params "threads=1:rc-lookahead=0" \
        output.mp4

        ;;

    time)

        /usr/bin/time -v \
        "${FFMPEG}" -y \
        -threads 1 \
        -framerate 10 \
        -start_number 0 \
        -i "rotation-%04d.png" \
        -c:v libx264 \
        -pix_fmt yuv420p \
        -preset veryfast \
        "${OUTPUT_FILE}"

        ;;

    create_animation)

        "${FFMPEG}" -y \
        -framerate 10 \
        -start_number 0 \
        -i "rotation-%04d.png" \
        -c:v libx264 \
        -pix_fmt yuv420p \
        -preset veryfast \
        "${OUTPUT_FILE}"

        ;;

    create_animation_optimised)

        # -preset ultrafast \

        # "${FFMPEG}" -y \
        # -threads 1 \
        # -framerate 10 \
        # -start_number 0 \
        # -i "rotation-%04d.png" \
        # -c:v libx264 \
        # -threads:v 1 \
        # -pix_fmt yuv420p \
        # -tune zerolatency \
        # -x264-params "threads=1:rc-lookahead=0" \
        # "${OUTPUT_FILE}"

        "${FFMPEG}" -y \
        -threads 1 \
        -framerate 10 \
        -start_number 0 \
        -i "rotation-%04d.png" \
        -c:v libx264 \
        -threads:v 1 \
        -preset medium \
        -tune zerolatency \
        -x264-params "threads=1:rc-lookahead=0" \
        -crf 18 \
        -pix_fmt yuv420p \
        "${OUTPUT_FILE}"

        ;;

    *)
        echo "Option not recognised!"

        ;;
esac


exit 0