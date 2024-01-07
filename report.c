#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_LINE_LENGTH 256
#define MAX_DATE_LENGTH 11

// Structure to store weather data
struct WeatherData {
    char date[MAX_DATE_LENGTH];
    char time[9];
    float temperature;
    float feels_like;
    float min_temperature;
    float max_temperature;
    int pressure;
    int humidity;
    char weather_description[MAX_LINE_LENGTH];
};

int main() {
    char city_name[50];
    printf("Enter the city name: ");
    scanf("%s", city_name);

    // Create file name based on the city name
    char file_name[100];
    sprintf(file_name, "%s_database.txt", city_name);

    // Open the file for reading
    FILE *file = fopen(file_name, "r");
    if (file == NULL) {
        printf("Error opening file %s\n", file_name);
        return 1;
    }

    // Initialize variables for reading lines and weather data
    char line[MAX_LINE_LENGTH];
    struct WeatherData *data = NULL; // Dynamic array to store weather data
    int entry_count = 0;
    int array_size = 10; // Initial size of the dynamic array

    // Dynamically allocate memory for the array
    data = (struct WeatherData *)malloc(array_size * sizeof(struct WeatherData));

    if (data == NULL) {
        printf("Memory allocation error\n");
        fclose(file);
        return 1;
    }

    // Loop through lines in the file
    while (fgets(line, sizeof(line), file) != NULL) {
        // Check for the start of a new data entry
        if (strncmp(line, "Time: ", 6) == 0) {
            // Resize the dynamic array if needed
            if (entry_count == array_size) {
                array_size *= 2;
                data = (struct WeatherData *)realloc(data, array_size * sizeof(struct WeatherData));

                if (data == NULL) {
                    printf("Memory reallocation error\n");
                    fclose(file);
                    return 1;
                }
            }

            // Extract the date and time from the line
            sscanf(line, "Time: %10s %8s", data[entry_count].date, data[entry_count].time);

            // Extract other weather data from the corresponding lines
            fgets(line, sizeof(line), file);
            sscanf(line, "Temperature: %f", &data[entry_count].temperature);

            fgets(line, sizeof(line), file);
            sscanf(line, "Feels Like: %f", &data[entry_count].feels_like);

            fgets(line, sizeof(line), file);
            sscanf(line, "Min Temperature: %f", &data[entry_count].min_temperature);

            fgets(line, sizeof(line), file);
            sscanf(line, "Max Temperature: %f", &data[entry_count].max_temperature);

            fgets(line, sizeof(line), file);
            sscanf(line, "Pressure: %d", &data[entry_count].pressure);

            fgets(line, sizeof(line), file);
            sscanf(line, "Humidity: %d", &data[entry_count].humidity);

            fgets(line, sizeof(line), file); // Read and ignore the Weather description line

            // Increment the entry count for the next data
            entry_count++;
        }
    }

    // Close the file
    fclose(file);

    // Get the current date
    time_t t = time(NULL);
    struct tm tm = *localtime(&t);
    char current_date[MAX_DATE_LENGTH];
    sprintf(current_date, "%04d-%02d-%02d", tm.tm_year + 1900, tm.tm_mon + 1, tm.tm_mday);

    // Calculate averages for the current date and upcoming dates
    float avg_temperature = 0.0, avg_feels_like = 0.0, avg_min_temperature = 0.0,
          avg_max_temperature = 0.0;
    int avg_pressure = 0, avg_humidity = 0, valid_entries = 0;

    // Print averages for today's weather condition
    printf("\nToday's Weather Condition\n");
    for (int i = 0; i < entry_count; i++) {
        if (strcmp(data[i].date, current_date) == 0) {
            // Accumulate values for averages
            avg_temperature += data[i].temperature;
            avg_feels_like += data[i].feels_like;
            avg_min_temperature += data[i].min_temperature;
            avg_max_temperature += data[i].max_temperature;
            avg_pressure += data[i].pressure;
            avg_humidity += data[i].humidity;
            valid_entries++;
        }
    }

    if (valid_entries > 0) {
        // Calculate averages
        avg_temperature /= valid_entries;
        avg_feels_like /= valid_entries;
        avg_min_temperature /= valid_entries;
        avg_max_temperature /= valid_entries;
        avg_pressure /= valid_entries;
        avg_humidity /= valid_entries;

        // Print averages for today's weather condition
        printf("\nTemperature: %.2f\n", avg_temperature);
        printf("Feels Like: %.2f\n", avg_feels_like);
        printf("Min Temperature: %.2f\n", avg_min_temperature);
        printf("Max Temperature: %.2f\n", avg_max_temperature);
        printf("Pressure: %d\n", avg_pressure);
        printf("Humidity: %d\n", avg_humidity);
    } else {
        printf("No valid entries found for today's weather condition.\n");
    }

    // Reset variables for the next block
    avg_temperature = 0.0, avg_feels_like = 0.0, avg_min_temperature = 0.0, avg_max_temperature = 0.0;
    avg_pressure = 0, avg_humidity = 0, valid_entries = 0;

    // Print next 5-days forecast
    printf("\nNext 5-Days Forecast\n");
    for (int i = 0; i < entry_count; i++) {
        if (strcmp(data[i].date, current_date) > 0 && valid_entries < 5) {
            // Accumulate values for averages
            avg_temperature += data[i].temperature;
            avg_feels_like += data[i].feels_like;
            avg_min_temperature += data[i].min_temperature;
            avg_max_temperature += data[i].max_temperature;
            avg_pressure += data[i].pressure;
            avg_humidity += data[i].humidity;
            valid_entries++;
        }
    }

    if (valid_entries > 0) {
        // Calculate averages
        avg_temperature /= valid_entries;
        avg_feels_like /= valid_entries;
        avg_min_temperature /= valid_entries;
        avg_max_temperature /= valid_entries;
        avg_pressure /= valid_entries;
        avg_humidity /= valid_entries;

        // Print averages for next 5-days forecast
        printf("\nAverage Temperature: %.2f\n", avg_temperature);
        printf("Average Feels Like: %.2f\n", avg_feels_like);
        printf("Average Min Temperature: %.2f\n", avg_min_temperature);
        printf("Average Max Temperature: %.2f\n", avg_max_temperature);
        printf("Average Pressure: %d\n", avg_pressure);
        printf("Average Humidity: %d\n", avg_humidity);
    } else {
        printf("No valid entries found for next 5-days forecast.\n");
    }

    // Free dynamically allocated memory
    free(data);

    return 0;
}
